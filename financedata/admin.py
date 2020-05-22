from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin


class InternalCostAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("proposal__name",)
    raw_id_fields = ("proposal",)
    list_display = ("entity","proposal","cost","cost_category","total_amount")
    
    def get_form(self, request, obj=None, **kwargs):
        internal_company_list = ['Samhita Social Ventures','Collective Good Foundation']
        form = super(InternalCostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['entity'].queryset = Profile.objects.filter(name__in=internal_company_list)
        return form

class SubisdiaryDisbursementAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("proposal__name",)
    raw_id_fields = ("subsidiary","proposal")
    list_display = ("subsidiary","proposal","cost","cost_category","total_amount")

admin.site.register(InternalCost,InternalCostAdmin)
admin.site.register(SubisdiaryDisbursement,SubisdiaryDisbursementAdmin)