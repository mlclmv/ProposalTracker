from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from masterdata.models import CostCategory
from organization.models import Profile
from KYPSamhita.models import Proposal

class InternalCost(models.Model):
    entity = models.ForeignKey(Profile,verbose_name="Internal Entity",on_delete=models.PROTECT,blank=True,null=True,related_name="entity_fk")
    cost = models.CharField(default="General",max_length=200)
    cost_category = models.ForeignKey(CostCategory,verbose_name="Cost Category",on_delete=models.PROTECT,blank=True,null=True,related_name="costcategory_fk")
    rate = models.PositiveIntegerField("Cost Rate/Value", blank=True, null=True)
    nos = models.PositiveIntegerField("Nos.",default=1, blank=True, null=True)
    unit = models.CharField(default="nos.",max_length=200,blank=True, null=True)
    total_amount = models.PositiveIntegerField("Total Amount", default=0)
    proposal = models.ForeignKey(Proposal,on_delete=models.PROTECT,related_name="intcost_proposal",blank=True, null=True)

    def __unicode__(self):
        return self.cost or ''

    def __str__(self):
        return self.cost or ''

class SubisdiaryDisbursement(models.Model):
    subsidiary = models.ForeignKey(Profile,verbose_name="Subsidiary Organization",on_delete=models.PROTECT,blank=True,null=True,related_name="subsidiary_fk")
    cost = models.CharField(default="General",max_length=200)
    cost_category = models.ForeignKey(CostCategory,verbose_name="Cost Category",default=1,on_delete=models.PROTECT,blank=True,null=True,related_name="subsidiary_costcategory_fk")
    rate = models.PositiveIntegerField("Cost Rate/Value", blank=True, null=True)
    nos = models.PositiveIntegerField("Nos.",default=1, blank=True, null=True)
    unit = models.CharField(default="nos.",max_length=200)
    total_amount = models.PositiveIntegerField("Total Amount",default=0)
    proposal = models.ForeignKey(Proposal,on_delete=models.PROTECT,related_name="subdisb_proposal",blank=True, null=True)

    def __unicode__(self):
        return self.cost or ''

    def __str__(self):
        return self.cost or ''
