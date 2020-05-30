from django.contrib import admin
from .models import Proposal, ProposalDoc
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from cities_light.models import City,Region
from cities_light.admin import RegionAdmin,CityAdmin
from financedata.models import InternalCost,SubsidiaryDisbursement
from KYPSamhita.models import Profile
from django.forms import ModelForm
# Register your models here.

class PDInlineAdmin(admin.TabularInline):
    model = ProposalDoc
    fields = ("stage","name","date","doc")
    list_display = ("proposal","name","date","doc")
    extra = 1


class ICInlineForm(ModelForm):
  def __init__(self, *args, **kwargs):
    internal_company_list = ['Samhita Social Ventures','Collective Good Foundation']
    super(ICInlineForm, self).__init__(*args, **kwargs)
    self.fields['entity'].queryset = Profile.objects.filter(name__in=internal_company_list)
                 
class ICInlineAdmin(admin.TabularInline):
    form = ICInlineForm
    model = InternalCost
    fields = ("entity","cost","cost_category","rate","nos","unit","total_amount")
    list_display = ("entity","cost","cost_category","total_amount")
    extra = 1
class SDInlineAdmin(admin.TabularInline):
    model = SubsidiaryDisbursement
    raw_id_fields = ("subsidiary",)
    fields = ("subsidiary","cost","cost_category","rate","nos","unit","total_amount")
    list_display = ("subsidiary","cost","cost_category","total_amount")
    extra = 1

class ProposalAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    filter_horizontal = ("service","imp_partner")
    list_display = ("name","organization","spoc")
    inlines = (ICInlineAdmin,SDInlineAdmin,PDInlineAdmin)
    class Meta:
        model = Proposal
    
class ProposalDocAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("name","date","doc","proposal","stage")

class StateAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    pass

class RegionCityAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    pass

admin.site.register(ProposalDoc,ProposalDocAdmin)
admin.site.register(Proposal,ProposalAdmin)
admin.site.unregister(Region)
admin.site.register(Region,StateAdmin)
admin.site.unregister(City)
admin.site.register(City,RegionCityAdmin)