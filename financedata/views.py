from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput,inlineformset_factory, formset_factory
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.conf import settings
from funky_sheets.formsets import HotView
from .models import InternalCost,SubsidiaryDisbursement,Proposal,Profile
from django.shortcuts import render 
from .forms import ICForm 

def IC_view(request, prop_id):
    prop_obj = Proposal.objects.get(id=prop_id)
    ic_obj = InternalCost.objects.filter(proposal__id=prop_id)
    ICFormSet = inlineformset_factory(Proposal,InternalCost, form=ICForm,extra =1)
    formset = ICFormSet(queryset=InternalCost.objects.none(),instance = prop_obj)
    if request.method == "POST":
        formset = ICFormSet(request.POST,instance= prop_obj)
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy('financeapp:ic-form' , kwargs={'prop_id': prop_id}))
    
    return render(request, 'ic_form.html', {'formset': formset})


class AddInterncalCost(HotView):
    
    model = InternalCost
    
    template_name = 'ic_add.html'
    
    checkbox_checked = 'yes' 
    checkbox_unchecked = 'no' 
    
    prefix = 'table'
    
    success_url = reverse_lazy('financeapp:update-ic')
    
    fields = ("id","cost","entity","cost_category","proposal","nos","rate","unit","total_amount")
    
    hot_settings = {
        'licenseKey': 'non-commercial-and-evaluation',
        'dropdownmenu' : 'true',
        'headerTooltips': {
            'rows': 'true',
            'columns': 'true'
        }
    }

class UpdateInternalCost(AddInterncalCost):
    template_name = 'ic_update.html'
    action = 'update'
    button_text = 'Update'

    hot_settings = {
        'licenseKey': 'non-commercial-and-evaluation',
        'headerTooltips': {
            'rows': 'true',
            'columns': 'true'
        },
    }

