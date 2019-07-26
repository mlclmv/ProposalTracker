from cities_light.models import City,Region
from django.db import models
from django.conf import settings
from masterdata.models import CauseArea
from organization.models import Profile

class ProgramInfo(models.Model):
    name = models.CharField(unique=True,max_length=200)
    description = models.TextField(blank=True, null=True)
    cause_area = models.ManyToManyField(CauseArea, help_text='Cause Area', blank=True)
    location_state = models.ManyToManyField(Region,help_text="Select State(s) in which program was conducted",blank=True,related_name="prog_state",verbose_name="State(s)")
    location_city = models.ManyToManyField(City,help_text="Select State(s) in which program was conducted",blank=True,related_name="prog_city",verbose_name="Cities")
    organization = models.ForeignKey(Profile,on_delete=models.SET_NULL,related_name="prog_org",blank=True, null=True)
    beneficiaries = models.PositiveIntegerField("No. of beneficiaries impacted", blank=True, null=True)
    value = models.PositiveIntegerField("Budget/Value of Program", blank=True, null=True)
    imp_partner =  models.ManyToManyField(Profile, blank=True,related_name="progimp_partner",help_text="Pick Implementation Partner")

    def __unicode__(self):
        return self.name or ''

    def __str__(self):
        return self.name or ''
