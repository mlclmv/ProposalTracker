from django.contrib import admin
from .models import ProgramInfo
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProgramAdmin(ImportExportModelAdmin):
    filter_horizontal = ('cause_area','location_state','location_city','imp_partner')
    list_display = ("name","organization","value")

admin.site.register(ProgramInfo,ProgramAdmin)