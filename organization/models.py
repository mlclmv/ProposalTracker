from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid,time
from django import forms
from django.db import models
from django.conf import settings
from masterdata.models import Industry,OrganizationType,CauseArea,EngagementType,Question,PartnershipLevel,RiskLevel
from cities_light.models import City,Region
from slugify import slugify

def get_upload_to(instance, filename):
    ftime = time.localtime()
    try:
        return 'org_file/%s/%s/%s/%s' % (slugify(instance.name), ftime.tm_year, ftime.tm_mon, filename)
    except:
        return 'org_file/other/%s/%s/%s' % (ftime.tm_year, ftime.tm_mon, filename)

class Profile(models.Model):
    name = models.CharField("Organization name",unique=True,max_length=200)
    office_location = models.ManyToManyField(City,help_text="Select a location",blank=True,related_name="org_hq",verbose_name="Head Office Location")
    vision = models.TextField(help_text="Vision Statement", blank=True, null=True)
    industry = models.ManyToManyField(Industry,blank=True,related_name="org_details", help_text="Area of work")
    org_type = models.ForeignKey(OrganizationType,"Type of Organization",blank=True,null=True)
    cause_area = models.ManyToManyField(CauseArea, help_text='CSR Priorities', blank=True)
    location_state = models.ManyToManyField(Region,help_text="States with geographical presence",blank=True,related_name="org_state",verbose_name="CSR Activity - States")
    location_city = models.ManyToManyField(City,help_text="Cities with geographical presence",blank=True,related_name="org_city",verbose_name="CSR Activity - Cities")
    csr_budget = models.PositiveIntegerField(blank=True, null=True)
    statements = models.FileField(help_text ="Financial Statements - Last 3 years", upload_to=get_upload_to, null=True, blank=True)
    partner_level = models.ForeignKey(PartnershipLevel, on_delete=models.PROTECT,blank=True,null=True,related_name="partner_level")
    engagement_type = models.ManyToManyField(EngagementType, help_text='Type of engagement', blank=True)
    main_partner = models.ForeignKey('self', on_delete=models.PROTECT, help_text='Exclusive partner if any ', blank=True, null=True)
    partners = models.ManyToManyField('self', help_text='Other Partners', blank=True)
    head_name = models.CharField(help_text="Name of Organization head",max_length=200,blank=True,null=True)
    head_position = models.CharField(help_text="Position of Organization head",max_length=200,blank=True,null=True)
    head_email = models.EmailField(help_text="Email of Organization head",max_length=70,blank=True,null=True)
    spoc_name = models.CharField(help_text="Name of SPOC",max_length=200,blank=True,null=True)
    spoc_position = models.CharField(help_text="Position of SPOC",max_length=200,blank=True,null=True)
    spoc_email = models.EmailField(help_text="Email of SPOC",max_length=70,blank=True,null=True)
    mkt_position = models.TextField(help_text="Market positioning", blank=True, null=True)
    risk_level = models.ForeignKey(RiskLevel, on_delete=models.PROTECT,blank=True,null=True,related_name="risk_level")
    risks= models.TextField(help_text="Risks associated (Reputation/ Default etc.)Risks associated (Reputation/ Default etc.)", blank=True, null=True)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class StrategyChecklist(models.Model):
    organization = models.ForeignKey(Profile,"Organization")
    qt1 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq1",default=1,verbose_name="Q")
    q1 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt2 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq2",default=2,verbose_name="Q")
    q2 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt3 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq3",default=3,verbose_name="Q")
    q3 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")

    def __unicode__(self):
        return self.organization.name or ''

    def __str__(self):
        return self.organization.name or ''

class StructureChecklist(models.Model):
    organization = models.ForeignKey(Profile,"Organization")
    qt1 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq4",default=4,verbose_name="Q")
    q1 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt2 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq5",default=5,verbose_name="Q")
    q2 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt3 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq6",default=6,verbose_name="Q")
    q3 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")

    def __unicode__(self):
        return self.organization.name or ''

    def __str__(self):
        return self.organization.name or ''

class ProcessPracticeChecklist(models.Model):
    organization = models.ForeignKey(Profile,"Organization")
    qt1 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq7",default=7,verbose_name="Q")
    q1 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt2 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq8",default=8,verbose_name="Q")
    q2 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt3 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq9",default=9,verbose_name="Q")
    q3 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")

    def __unicode__(self):
        return self.organization.name or ''

    def __str__(self):
        return self.organization.name or ''

class PeopleChecklist(models.Model):
    organization = models.ForeignKey(Profile,"Organization")
    qt1 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq10",default=10,verbose_name="Q")
    q1 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt2 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq11",default=11,verbose_name="Q")
    q2 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")
    qt3 = models.ForeignKey(Question,on_delete=models.PROTECT,related_name="scq12",default=12,verbose_name="Q")
    q3 = models.NullBooleanField(choices=settings.BOOL_CHOICES,verbose_name="A")

    def __unicode__(self):
        return self.organization.name or ''

    def __str__(self):
        return self.organization.name or ''