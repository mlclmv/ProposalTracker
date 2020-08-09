import datetime
from django.db import models
from django.conf import settings
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from masterdata.models import ProposalStage, Service, Workflow, ProposalStatus
from organization.models import Profile
# from simple_history.models import HistoricalRecords


class Proposal(models.Model):
    name = models.CharField(unique=True,max_length=200)
    status = models.ForeignKey(ProposalStatus,on_delete=models.PROTECT,related_name="prop_status",blank=True, null=True,default=1)
    description = models.TextField(blank=True, null=True)
    organization = models.ForeignKey(Profile,on_delete=models.SET_NULL,related_name="org",blank=True, null=True)
    value = models.PositiveIntegerField("Budget/Value of Proposal", blank=True, null=True)
    service = models.ManyToManyField(Service,blank=True,help_text="Service Engaged")
    imp_partner =  models.ManyToManyField(Profile, blank=True,related_name="imp_partner",help_text="Pick Implementation Partner")
    spoc = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT, blank=True, null=True,help_text="Proposal Handler")
    slug = models.SlugField(unique=True,null=True,blank=True)
    workflow = models.ForeignKey(Workflow,on_delete=models.PROTECT,related_name="prop_workflow",blank=True, null=True,default=1)
    stage = models.ForeignKey(ProposalStage,verbose_name='Current Stage',on_delete=models.PROTECT,related_name="prop_stage",blank=True, null=True)
    # history = HistoricalRecords()

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Proposal.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    # def modified_date(self):
    #     try:
    #         modified_datetime = self.history.last().history_date
    #     except:
    #         modified_datetime = None
    #     return modified_datetime

# Signal to create Proposal document on Proposal creation
# @receiver(post_save, sender=Proposal)
# def proposal_doc_creation(sender, **kwargs):
#     proposal_obj = kwargs['instance']
#     try:
#         stage,created = ProposalStage.objects.get_or_create(name="Proposal sent/received",workflow__id=2,order=1,recurring=False)
#         def_workflow = Workflow.objects.get(pk=1)
#         def_stage = ProposalStage.objects.filter(workflow=def_workflow,order=1).first()
#         if (ProposalDoc.objects.filter(name="Proposal Document",proposal=proposal_obj,stage=stage)):
#             print ("<Proposal Doc exists> : New Document creation aborted")
#         else:
#             proposal_doc,created = ProposalDoc.objects.get_or_create(name="Proposal Document",proposal=proposal_obj,workflow__id=2,stage=stage)
#         mou_doc,created = ProposalDoc.objects.get_or_create(name="MoU signed",proposal=proposal_obj,stage=def_stage,workflow=def_workflow)
#     except Exception as e:
#         print ("<ProposalDocCreationError>",e)

class ProposalDoc(models.Model):
    modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200,blank=True, null=True)
    date = models.DateField("Date/Month of Doc/Report",default=datetime.date.today)
    proposal = models.ForeignKey(Proposal,on_delete=models.PROTECT,related_name="doc_proposal",blank=True, null=True)
    workflow = models.ForeignKey(Workflow,on_delete=models.PROTECT,related_name="doc_workflow",blank=True, null=True,default=1)
    stage = models.ForeignKey(ProposalStage,on_delete=models.PROTECT,related_name="doc_stage",blank=True, null=True)
    doc = models.FileField(help_text ="Upload file", upload_to="proposal_docs/%Y-%m/", null=True, blank=True)


    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''
