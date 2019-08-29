from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from . import models
from KYPSamhita.models import Proposal,ProposalDoc
from program.models import ProgramInfo
from masterdata.models import *
from organization.models import StrategyChecklist,StructureChecklist,ProcessPracticeChecklist,PeopleChecklist
from django.http import JsonResponse
from cities_light.models import City
from django.contrib.auth import get_user_model

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
                services_off = proposal.service.all()
            except Exception as e:
                print ('<ServiceOffError>: ',e)
            try:
                proposal_stages = ProposalStage.objects.filter(workflow__name="Good Governance").order_by("order")
            except Exception as e:
                print ('<PropStageError>: ',e)
            try:
                proposal_docs = ProposalDoc.objects.filter(workflow__name="Good Governance",proposal=proposal).order_by("date","modified_date")
            except Exception as e:
                print ('<PropDocError>: ',e)
            try:
                prop_file = ProposalDoc.objects.get(stage__name="Proposal sent/received",proposal=proposal)
                if prop_file.doc:
                    prop_sent = True
            except Exception as e:
                print ('<PropSentError>: ',e)
            try:
                mou_file = ProposalDoc.objects.filter(name__icontains="mou",workflow__name="Good Governance",proposal=proposal).order_by("date","modified_date").first()
                if mou_file.doc:
                    mou_signed = True
            except Exception as e:
                print ('<PropDocError>: ',e)
            try:
                projstart_file = ProposalDoc.objects.filter((Q(name__icontains="mom")|Q(name__icontains="minutes")), workflow__name="Good Governance",proposal=proposal).first()
                if projstart_file.doc:
                    projstart = True
            except Exception as e:
                print ('<ProjStartError>: ',e)
            try:
                projreport_file = ProposalDoc.objects.filter((Q(name__icontains="monthly")|Q(name__icontains="quarterly")|Q(name__icontains="report")|Q(name__icontains="reports")), workflow__name="Good Governance",stage__order=2,proposal=proposal).first()
                if projreport_file.doc:
                    projreport = True
            except Exception as e:
                print ('<ProjReportError>: ',e)
            try:
                impactreport_file = ProposalDoc.objects.filter(workflow__name="Good Governance",stage__order=3,proposal=proposal).first()
                if impactreport_file.doc:
                    impactreport = True
            except Exception as e:
                print ('<ImpactReportError>: ',e)
            try:
                finreview_file = ProposalDoc.objects.filter(workflow__name="Good Governance",stage__order=4,proposal=proposal).first()
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

def ListingPage(request):
    User = get_user_model()
    proposal_list = Proposal.objects.filter(id__in=['1','11'])
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
    m_partner_level = PartnershipLevel.objects.all()
    m_city = City.objects.all()
    m_industry = Industry.objects.all()
    m_risk = RiskLevel.objects.all()
    m_service = Service.objects.all()
    m_type = EngagementType.objects.all()
    m_cause = CauseArea.objects.all()
    m_poc = User.objects.all()
    m_status = ProposalStage.objects.all()
    m_budget = [{"id":1,"name":"0-10L"},{"id":2,"name":"10L-50L"},{"id":3,"name":"50L-1CR"},{"id":4,"name":"1CR-10CR"},{"id":5,"name":"10CR and above"}]
    for i in proposal_list:
        try:
            proposal = Proposal.objects.filter(id=i.id).first()
            if proposal != None:
                prop_details[i.id] = proposal
                print ("prop_d",prop_details)
                try:
                    org[i.id] = proposal.organization
                    print(org[i.id])
                    if org[i.id]:
                        try:
                            partner_level[i.id] = org[i.id].partner_level
                        except Exception as e:
                            partner_level[i.id] = "Level not set"
                        print ('partnerlevel',partner_level)
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
                    mou_file[i.id] = ProposalDoc.objects.filter(name__icontains="mou",workflow__name="Good Governance",proposal=proposal).order_by("-date","-modified_date").first()
                except Exception as e:
                    print ('<PropDocError>: ',e)
                try:
                    projstart_file[i.id] = ProposalDoc.objects.filter((Q(name__icontains="mom")|Q(name__icontains="minutes")), workflow__name="Good Governance",proposal=proposal).first()
                except Exception as e:
                    print ('<ProjStartError>: ',e)
                try:
                    projreport_file[i.id] = ProposalDoc.objects.filter((Q(name__icontains="monthly")|Q(name__icontains="quarterly")|Q(name__icontains="report")|Q(name__icontains="reports")), workflow__name="Good Governance",stage__order=2,proposal=proposal).first()
                except Exception as e:
                    print ('<ProjReportError>: ',e)
                try:
                    impactreport_file[i.id] = ProposalDoc.objects.filter(workflow__name="Good Governance",stage__order=3,proposal=proposal).first()
                except Exception as e:
                    print ('<ImpactReportError>: ',e)
                try:
                    finreview_file[i.id] = ProposalDoc.objects.filter(workflow__name="Good Governance",stage__order=4,proposal=proposal).first()
                except Exception as e:
                    print ('<FinReportError>: ',e)
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
        print ("comp",kyp_comp)
    return render(request,'../templates/listing.html',locals())