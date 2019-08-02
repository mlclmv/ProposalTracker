from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models
from KYPSamhita.models import Proposal
from program.models import ProgramInfo

def ProposalPage(request,proposal_slug):
    proposal = ""
    org = ""
    partner_level = ""
    risk_level = ""
    services_off = ""
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
            
    except:
        proposal = ""
    return render(request,'../templates/home.html',locals())