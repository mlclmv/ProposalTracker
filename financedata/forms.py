from django import forms 
from django.conf import settings
from .models import Profile,Proposal,CostCategory,InternalCost

try:
    get_def_entity = Profile.objects.filter(name=settings.INTERNAL_COMPANIES[0]).first()
except:
    get_def_entity = 1


class ICForm(forms.ModelForm): 
    entity = forms.ModelChoiceField(label="Internal entity",queryset=Profile.objects.filter(name__in=settings.INTERNAL_COMPANIES),initial=get_def_entity.id)
    cost = forms.CharField(label="Item",max_length = 200, initial = "Generic")
    cost_category = forms.ModelChoiceField(label="Category",queryset=CostCategory.objects.all(),initial= 1)
    rate = forms.IntegerField(required=False)
    unit = forms.CharField(max_length = 200,required=False, initial = "unit")
    nos = forms.IntegerField(label="No. of units",required=False, initial = 1)
    total_amount = forms.IntegerField(label="Total", initial = 0)
    proposal = forms.ModelChoiceField(queryset=Proposal.objects.all())


    class Meta:
        model = InternalCost
        fields = "__all__"