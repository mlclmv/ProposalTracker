from django.contrib import admin
from .models import Profile, StrategyChecklist, StructureChecklist, ProcessPracticeChecklist, PeopleChecklist
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class StrategyInlineAdmin(admin.StackedInline):
    model = StrategyChecklist
    fields = ("qt1","q1","qt2","q2","qt3","q3")
    readonly_fields = ("qt1","qt2","qt3")
    list_display = ("organization","q1","q2","q3")
    extra = 1
    max_num = 1

class StructureInlineAdmin(admin.StackedInline):
    model = StructureChecklist
    fields = ("qt1","q1","qt2","q2","qt3","q3")
    readonly_fields = ("qt1","qt2","qt3")
    list_display = ("organization","q1","q2","q3")
    extra = 1
    max_num = 1

class ProcessPracticeInlineAdmin(admin.StackedInline):
    model = ProcessPracticeChecklist
    fields = ("qt1","q1","qt2","q2","qt3","q3")
    readonly_fields = ("qt1","qt2","qt3")
    list_display = ("organization","q1","q2","q3")
    extra = 1
    max_num = 1


class PeopleInlineAdmin(admin.StackedInline):
    model = PeopleChecklist
    fields = ("qt1","q1","qt2","q2","qt3","q3")
    readonly_fields = ("qt1","qt2","qt3")
    list_display = ("organization","q1","q2","q3")
    extra = 1
    max_num = 1

class ProfileAdmin(ImportExportModelAdmin):
    filter_horizontal = ('office_location','location_state','location_city','industry','partners','cause_area','engagement_type')
    list_display = ("name","head_name","spoc_name")
    inlines = (StrategyInlineAdmin,StructureInlineAdmin,ProcessPracticeInlineAdmin,PeopleInlineAdmin)
    class Meta:
        model = Profile

class StrategyCLAdmin(ImportExportModelAdmin):
    list_display = ("organization","q1","q2","q3")

class StructureCLAdmin(ImportExportModelAdmin):
    list_display = ("organization","q1","q2","q3")

class ProcessPracticeCLAdmin(ImportExportModelAdmin):
    list_display = ("organization","q1","q2","q3")

class PeopleCLAdmin(ImportExportModelAdmin):
    list_display = ("organization","q1","q2","q3")

admin.site.register(Profile,ProfileAdmin)
admin.site.register(StrategyChecklist,StrategyCLAdmin)
admin.site.register(StructureChecklist,StructureCLAdmin)
admin.site.register(ProcessPracticeChecklist,ProcessPracticeCLAdmin)
admin.site.register(PeopleChecklist,PeopleCLAdmin)