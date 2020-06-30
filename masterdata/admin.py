from django.contrib import admin
from .models import (CauseArea,Industry,OrganizationType,ProposalStage,
Service,Workflow,EngagementType,Department,Question,PartnershipLevel,RiskLevel,BudgetCategory,CostCategory,ProposalStatus)
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin

# Register your models here.
class CauseAreaAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name",)

class IndustryAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name",)

class OrgTypeAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name",)

class EngageTypeAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name","description")

class WorkFlowAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name",)

class PropStageAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    filter_horizontal = ("dependency",)
    list_display = ("id","name","workflow","order","recurring")

class ServiceAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    filter_horizontal = ("department",)
    list_display = ("id","name",)

class DeptAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name")

class QuestionAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","question","order")

class PartnerLevelAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name","description")

class RiskLevelAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name","description")

class BudgetCategoryAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name","description")

class CostCategoryAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
    list_display = ("id","name","budget_category")

class PropStatusAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin):
    search_fields = ("name",)
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
admin.site.register(RiskLevel,RiskLevelAdmin)
admin.site.register(BudgetCategory,BudgetCategoryAdmin)
admin.site.register(CostCategory,CostCategoryAdmin)
admin.site.register(ProposalStatus,PropStatusAdmin)