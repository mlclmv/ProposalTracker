from django.contrib import admin
from .models import CauseArea,Industry,OrganizationType,ProposalStage,Service,Workflow,EngagementType,Department,Question,PartnershipLevel
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CauseAreaAdmin(ImportExportModelAdmin):
    list_display = ("id","name",)

class IndustryAdmin(ImportExportModelAdmin):
    list_display = ("id","name",)

class OrgTypeAdmin(ImportExportModelAdmin):
    list_display = ("id","name",)

class EngageTypeAdmin(ImportExportModelAdmin):
    list_display = ("id","name","description")

class WorkFlowAdmin(ImportExportModelAdmin):
    list_display = ("id","name",)

class PropStageAdmin(ImportExportModelAdmin):
    filter_horizontal = ("dependency",)
    list_display = ("id","name","workflow","order","recurring")

class ServiceAdmin(ImportExportModelAdmin):
    filter_horizontal = ("department",)
    list_display = ("id","name",)

class DeptAdmin(ImportExportModelAdmin):
    list_display = ("id","name")

class QuestionAdmin(ImportExportModelAdmin):
    list_display = ("id","question","order")

class PartnerLevelAdmin(ImportExportModelAdmin):
    list_display = ("id","name","description")

admin.site.register(CauseArea,CauseAreaAdmin)
admin.site.register(Industry,IndustryAdmin)
admin.site.register(OrganizationType,OrgTypeAdmin)
admin.site.register(Workflow,WorkFlowAdmin)
admin.site.register(ProposalStage,PropStageAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(EngagementType,EngageTypeAdmin) 
admin.site.register(Department,DeptAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(PartnershipLevel,PartnerLevelAdmin)