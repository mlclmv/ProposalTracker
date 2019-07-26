import datetime
from django.db import models
from django.conf import settings
from masterdata.models import ProposalStage, Service, Workflow
from organization.models import Profile

class Proposal(models.Model):
    name = models.CharField(unique=True,max_length=200)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(Profile,on_delete=models.SET_NULL,related_name="org",blank=True, null=True)
    value = models.PositiveIntegerField("Budget/Value of Proposal", blank=True, null=True)
    service = models.ManyToManyField(Service,blank=True,help_text="Service Engaged")
    imp_partner =  models.ManyToManyField(Profile, blank=True,related_name="imp_partner",help_text="Pick Implementation Partner")
    spoc = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, blank=True, null=True,help_text="Proposal Handler")

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class ProposalDoc(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200,blank=True, null=True)
    date = models.DateField("Date/Month of Doc/Report",default=datetime.date.today)
    proposal = models.ForeignKey(Proposal,on_delete=models.PROTECT,related_name="doc_proposal",blank=True, null=True)
    workflow = models.ForeignKey(Workflow,on_delete=models.PROTECT,related_name="doc_workflow",blank=True, null=True,default=1)
    stage = models.ForeignKey(ProposalStage,on_delete=models.PROTECT,related_name="doc_stage",blank=True, null=True)
    doc = models.FileField(unique=True,help_text ="Upload file", upload_to="proposal_docs/%Y-%m/", null=True, blank=True)


    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''
