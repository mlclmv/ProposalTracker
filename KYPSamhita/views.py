from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from . import models
from KYPSamhita.models import Proposal,ProposalDoc
from program.models import ProgramInfo
from masterdata.models import *
from financedata.models import InternalCost,SubsidiaryDisbursement
from organization.models import Profile,StrategyChecklist,StructureChecklist,ProcessPracticeChecklist,PeopleChecklist
from django.http import JsonResponse
from cities_light.models import City
from django.contrib.auth import get_user_model

def getICListing(prop_id):
    ic_obj = InternalCost.objects.filter(proposal__id = prop_id)
    return ic_obj

def getSDListing(prop_id):
    sd_obj = SubsidiaryDisbursement.objects.filter(proposal__id = prop_id)
    return sd_obj

@login_required
def ProposalPage(request,proposal_slug):
    proposal = ""
    org = ""
    partner_level = ""
    risk_level = ""
    services_off = ""
    kyp_comp = 0
    prop_sent = False
    mou_signed = False
    projstart_file = False
    try:
        proposal = Proposal.objects.filter(slug=proposal_slug).first()
        if proposal != None:
            try:
                org = proposal.organization
                if org:
                    try:
                        partner_level = org.partner_level
                    except:
                        partner_level = "Level not set"
                    try:
                        risk_level = org.risk_level
                    except:
                        risk_level = "Level not set"
                    try:
                        programs = ProgramInfo.objects.filter(organization=org)
                    except:
                        programs = None                   
            except Exception as e:
                print ('<OrgNameError>: ',e)
            try:
                ic_list = getICListing(proposal.id)
            except Exception as e:
                print ('<ICListingError>',e) 
            try:
                sd_list = getSDListing(proposal.id)
            except Exception as e:
                print ('<SDListingError>',e) 
            try:
                services_off = proposal.service.all()
            except Exception as e:
                print ('<ServiceOffError>: ',e)
            try:
                proposal_stages = ProposalStage.objects.filter(workflow=proposal.workflow).order_by("order")
            except Exception as e:
                print ('<PropStageError>: ',e)
            try:
                proposal_status = ProposalStatus.objects.all().order_by("order")
            except Exception as e:
                print ('<PropStageError>: ',e)
            try:
                proposal_docs = ProposalDoc.objects.filter(workflow=proposal.workflow,proposal=proposal).order_by("date","modified_date")
            except Exception as e:
                print ('<PropDocError>: ',e)
            try:
                prop_file = ProposalDoc.objects.filter(stage__name="Proposal sent/received",proposal=proposal).first()
                if prop_file.doc:
                    prop_sent = True
            except Exception as e:
                print ('<PropSentError>: ',e)
            try:
                mou_file = ProposalDoc.objects.filter(name__icontains="mou",workflow=proposal.workflow,proposal=proposal).order_by("date","modified_date").first()
                if mou_file.doc:
                    mou_signed = True
            except Exception as e:
                print ('<PropDocError>: ',e)
            try:
                projstart_file = ProposalDoc.objects.filter((Q(name__icontains="mom")|Q(name__icontains="minutes")), workflow=proposal.workflow,proposal=proposal).first()
                if projstart_file.doc:
                    projstart = True
            except Exception as e:
                print ('<ProjStartError>: ',e)
            try:
                projreport_file = ProposalDoc.objects.filter((Q(name__icontains="monthly")|Q(name__icontains="quarterly")|Q(name__icontains="report")|Q(name__icontains="reports")), workflow=proposal.workflow,stage__order=2,proposal=proposal).first()
                if projreport_file.doc:
                    projreport = True
            except Exception as e:
                print ('<ProjReportError>: ',e)
            try:
                impactreport_file = ProposalDoc.objects.filter(workflow=proposal.workflow,stage__order=3,proposal=proposal).first()
                if impactreport_file.doc:
                    impactreport = True
            except Exception as e:
                print ('<ImpactReportError>: ',e)
            try:
                finreview_file = ProposalDoc.objects.filter(workflow=proposal.workflow,stage__order=4,proposal=proposal).first()
                if finreview_file.doc:
                    finreview = True
            except Exception as e:
                print ('<FinReportError>: ',e)
    except:
        proposal = ""
    # Get Strategy Questions
    try:
        q_strategy = Question.objects.filter(workflow__name="Strategy Check")
        a_strategy = StrategyChecklist.objects.filter(organization=org).last()
    except Exception as e:
        print ('<StratQuestionError>',e)
    # Get Structure Questions
    try:
        q_structure = Question.objects.filter(workflow__name="Structure")
        a_structure = StructureChecklist.objects.filter(organization=org).last()
    except Exception as e:
        print ('<StructQuestionError>',e)
    # Get Process & Practice Questions
    try:
        q_process = Question.objects.filter(workflow__name="Process and Practices")
        a_process = ProcessPracticeChecklist.objects.filter(organization=org).last()
    except Exception as e:
        print ('<PPQuestionError>',e)
    # Get People Questions
    try:
        q_people = Question.objects.filter(workflow__name="People")
        a_people = PeopleChecklist.objects.filter(organization=org).last()
    except Exception as e:
        print ('<PeopleQuestionError>',e)
    # Check KYP completion
    try:
        if (a_strategy.q1 != None and a_strategy.q2 != None and a_strategy.q3 != None):
            kyp_comp += 25
        if (a_structure.q1 != None and a_structure.q2 != None and a_structure.q3 != None):
            kyp_comp += 25
        if (a_process.q1 != None and a_process.q2 != None and a_process.q3 != None):
            kyp_comp += 25
        if (a_people.q1 != None and a_people.q2 != None and a_people.q3 != None):
            kyp_comp += 25
    except Exception as e:
        print ('<KYPcompError>',e)
    return render(request,'../templates/home.html',locals())

@login_required
def ListingPage(request):
    # Get POST data and initialize variables
    print('<Listing page>',request)
    form_data = {'partnerSearch':[], 'csrfmiddlewaretoken': []}
    search_text = ""
    get_filter = dict()
    try:
        for key, values in request.POST.lists():
            try:
                form_data[key] = [int(i) for i in values]
            except:
                form_data[key] = values
        print ("<FormData>", form_data)
        try:
            get_filter['organization__partner_level__id__in'] = form_data['level']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['organization__office_location__id__in'] = form_data['headquarter']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['organization__industry__id__in'] = form_data['industry']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['organization__risk_level__id__in'] = form_data['risk']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['service__id__in'] = form_data['service']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['organization__engagement_type__id__in'] = form_data['engagement']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['organization__location_city__id__in'] = form_data['location']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['organization__cause_area__id__in'] = form_data['cause']
        except Exception as e:
            print ("<FormDataException>", e)
        try:
            get_filter['spoc__id__in'] = form_data['spoc']
        except Exception as e:
            print ("<FormDataException>", e)
    except Exception as e:
        print ("<POSTDataException>", e)
    try:
        search_text = request.POST.get("partnerSearch","").strip()
    except Exception as e:
        print ("<SearchTextException>", e)
    try:
        get_filter['status__in'] = form_data['status']
    except Exception as e:
        print ("<StatusException>", e)
    try:
        get_filter['stage__in'] = form_data['stage']
    except Exception as e:
        print ("<StageException>", e)
    try:
        budget_min = int(request.POST.get("budget_min",""))
        get_filter['organization__csr_budget__gte'] = budget_min
    except Exception as e:
        print ("<BudgetMinException>", e)
    try:
        budget_max = int(request.POST.get("budget_max",""))
        get_filter['organization__csr_budget__lte'] = budget_max
    except Exception as e:
        print ("<BudgetMaxException>", e)
    # Initialize other variables
    User = get_user_model()
    proposal_list_all= Proposal.objects.filter((Q(name__icontains=search_text) | Q(organization__name__icontains=search_text) | Q(organization__org_type__name__icontains=search_text)\
                                            | Q(description__icontains=search_text) | Q(imp_partner__name__icontains=search_text)\
                                            | Q(spoc__name__icontains=search_text) | Q(service__name__icontains=search_text)\
                                            | Q(organization__cause_area__name__icontains=search_text) | Q(organization__partner_level__name__icontains=search_text)\
                                            | Q(organization__engagement_type__name__icontains=search_text) | Q(organization__head_name__icontains=search_text)\
                                            | Q(organization__location_state__name__icontains=search_text) | Q(organization__location_city__search_names__icontains=search_text)\
                                            | Q(organization__industry__name__icontains=search_text)),**get_filter).distinct().order_by("-id")
    paginator = Paginator(proposal_list_all,10)
    try:
        p_no = request.GET.get('page')
        page = paginator.get_page(p_no)
        proposal_list = page.object_list
        print ("dict",p_no,proposal_list)
    except:
        p_no = 1
        page = paginator.get_page(p_no)
        proposal_list = page.object_list
    proposal_dict = list(proposal_list.values("id"))
    proposal = {}
    prop_details = {}
    org = {}
    partner_level = {}
    risk_level = {}
    services_off = {}
    kyp_comp = {}
    prop_file = {}
    mou_file = {}
    projstart_file = {}
    projreport_file = {}
    impactreport_file = {}
    finreview_file = {}
    prop_stages = {}
    curr_stages = {}
    curr_status = {}
    m_partner_level = PartnershipLevel.objects.all()
    m_city = City.objects.all()
    m_industry = Industry.objects.all()
    m_risk = RiskLevel.objects.all()
    m_service = Service.objects.all()
    m_type = EngagementType.objects.all()
    m_cause = CauseArea.objects.all()
    m_poc = User.objects.all()
    m_status = ProposalStatus.objects.all().order_by('order')
    m_stage = ProposalStage.objects.all()
    m_budget = [{"id":0,"name":"INR 0 Rupee(s)"},{"id":1000000,"name":"INR 10 Lakh(s)"},{"id":5000000,"name":"INR 50 Lakh(s)"},{"id":10000000,"name":"INR 1 Crore(s)"},{"id":100000000,"name":"INR 10 Crore(s)"},{"id":1000000000,"name":"INR 100 Crore(s)"}]
    # Get all data for list page
    for i in proposal_list:
        try:
            proposal = Proposal.objects.filter(id=i.id).first()
            if proposal != None:
                prop_details[i.id] = proposal
                try:
                    org[i.id] = proposal.organization
                    if org[i.id]:
                        try:
                            partner_level[i.id] = org[i.id].partner_level
                        except Exception as e:
                            partner_level[i.id] = "Level not set"
                        try:
                            risk_level[i.id] = org[i.id].risk_level
                        except:
                            risk_level[i.id] = "Level not set"                
                except Exception as e:
                    print ('<OrgNameError>: ',e)
                try:
                    services_off[i.id] = proposal.service.all()
                except Exception as e:
                    print ('<ServiceOffError>: ',e)
                try:
                    prop_file[i.id] = ProposalDoc.objects.filter(stage__name="Proposal sent/received",proposal=proposal).order_by("-modified_date").first()
                except Exception as e:
                    print ('<PropSentError>: ',e)
                try:
                    mou_file[i.id] = ProposalDoc.objects.filter(name__icontains="mou",workflow=proposal.workflow,proposal=proposal).order_by("-date","-modified_date").first()
                except Exception as e:
                    print ('<PropDocError>: ',e)
                try:
                    projstart_file[i.id] = ProposalDoc.objects.filter((Q(name__icontains="mom")|Q(name__icontains="minutes")), workflow=proposal.workflow,proposal=proposal).first()
                except Exception as e:
                    print ('<ProjStartError>: ',e)
                try:
                    projreport_file[i.id] = ProposalDoc.objects.filter((Q(name__icontains="monthly")|Q(name__icontains="quarterly")|Q(name__icontains="report")|Q(name__icontains="reports")), workflow=proposal.workflow,stage__order=2,proposal=proposal).first()
                except Exception as e:
                    print ('<ProjReportError>: ',e)
                try:
                    impactreport_file[i.id] = ProposalDoc.objects.filter(workflow=proposal.workflow,stage__order=3,proposal=proposal).first()
                except Exception as e:
                    print ('<ImpactReportError>: ',e)
                try:
                    finreview_file[i.id] = ProposalDoc.objects.filter(workflow=proposal.workflow,stage__order=4,proposal=proposal).first()
                except Exception as e:
                    print ('<FinReportError>: ',e)
                # Get proposal workflow and stages 
                try:
                    prop_stages[i.id] = ProposalStage.objects.filter(workflow=proposal.workflow).order_by("order")
                except Exception as e:
                    print ('<PropStageError>: ',e)
                try:
                    curr_stages[i.id] = i.stage
                except Exception as e:
                    print ('<CurrStageError>: ',e)
                try:
                    curr_status[i.id] = i.status
                except Exception as e:
                    print ('<CurrStatusError>: ',e)
        except:
            proposal = ""
        # Get Strategy Questions
        try:
            q_strategy = Question.objects.filter(workflow__name="Strategy Check")
            a_strategy = StrategyChecklist.objects.filter(organization=org[i.id]).last()
        except Exception as e:
            print ('<StratQuestionError>',e)
        # Get Structure Questions
        try:
            q_structure = Question.objects.filter(workflow__name="Structure")
            a_structure = StructureChecklist.objects.filter(organization=org[i.id]).last()
        except Exception as e:
            print ('<StructQuestionError>',e)
        # Get Process & Practice Questions
        try:
            q_process = Question.objects.filter(workflow__name="Process and Practices")
            a_process = ProcessPracticeChecklist.objects.filter(organization=org[i.id]).last()
        except Exception as e:
            print ('<PPQuestionError>',e)
        # Get People Questions
        try:
            q_people = Question.objects.filter(workflow__name="People")
            a_people = PeopleChecklist.objects.filter(organization=org[i.id]).last()
        except Exception as e:
            print ('<PeopleQuestionError>',e)
        # Check KYP completion
        try:
            kyp_comp[i.id] = 0
            if (a_strategy and a_strategy.q1 != None and a_strategy.q2 != None and a_strategy.q3 != None):
                kyp_comp[i.id] += 25
            if (a_structure and a_structure.q1 != None and a_structure.q2 != None and a_structure.q3 != None):
                kyp_comp[i.id] += 25
            if (a_process and a_process.q1 != None and a_process.q2 != None and a_process.q3 != None):
                kyp_comp[i.id] += 25
            if (a_people and a_people.q1 != None and a_people.q2 != None and a_people.q3 != None):
                kyp_comp[i.id] += 25
        except Exception as e:
            kyp_comp[i.id] = 0
            print ('<KYPcompError>',e)
    return render(request,'../templates/listing.html',locals())