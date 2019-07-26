from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings

class Industry(models.Model):
    name = models.CharField(unique=True,max_length=200)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class CauseArea(models.Model):
    name = models.CharField(unique=True,max_length=200)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class Department(models.Model):
    name = models.CharField(unique=True,max_length=200)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class Workflow(models.Model):
    name = models.CharField(unique=True,max_length=200)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class ProposalStage(models.Model):
    name = models.CharField(max_length=200)
    workflow = models.ForeignKey(Workflow,on_delete=models.PROTECT,blank=True,null=True,related_name="stages")
    order = models.PositiveSmallIntegerField(blank=True, null=True)
    objective = models.TextField("Objectives",blank=True, null=True)
    good_practice = models.TextField("Good Practices",blank=True, null=True)
    output = models.CharField(max_length=200,blank=True, null=True)
    recurring = models.BooleanField(choices=settings.BOOL_CHOICES,verbose_name="Recurring Output?",blank=True,default=False)
    dependency = models.ManyToManyField('self',blank=True,related_name="dependency",verbose_name="Dependencies(if any)")

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return str(self.order)+'.'+self.name+'('+self.workflow.name+')' or ''

class Service(models.Model):
    name = models.CharField(unique=True,max_length=200)
    description = models.TextField(blank=True, null=True)
    department = models.ManyToManyField(Department,blank=True,related_name="service_dept")

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class OrganizationType(models.Model):
    name = models.CharField(unique=True,max_length=200)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class EngagementType(models.Model):
    name = models.CharField(unique=True,max_length=200)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class Question(models.Model):
    question = models.CharField(max_length=2000)
    workflow = models.ForeignKey(Workflow,on_delete=models.PROTECT,blank=True,null=True,related_name="workflow_fk")
    stage = models.OneToOneField(ProposalStage, on_delete=models.PROTECT,blank=True,null=True,related_name="stage_fk")
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.question or ''

    def __str__(self):
        return self.question or ''

class PartnershipLevel(models.Model):
    name = models.CharField(unique=True,max_length=200)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''

class RiskLevel(models.Model):
    name = models.CharField(unique=True,max_length=200)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''