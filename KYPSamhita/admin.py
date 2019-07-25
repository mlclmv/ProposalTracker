from django.contrib import admin
from .models import Proposal, ProposalDoc
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PDInlineAdmin(admin.TabularInline):
    model = ProposalDoc
    fields = ("stage","name","date","doc")
    list_display = ("proposal","name","date","doc")
    extra = 1

class ProposalAdmin(ImportExportModelAdmin):
    filter_horizontal = ('service','imp_partner')
    list_display = ("name","organization","spoc")
    inlines = (PDInlineAdmin,)
    class Meta:
        model = Proposal
    
class ProposalDocAdmin(ImportExportModelAdmin):
    list_display = ("name","date","doc","proposal","stage")

admin.site.register(ProposalDoc,ProposalDocAdmin)
admin.site.register(Proposal,ProposalAdmin)