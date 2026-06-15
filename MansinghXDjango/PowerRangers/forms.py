from django import forms
from .models import RangerTypes

class RangerTypesForm(forms.FORM):
    ranger_type = forms.ModelChoiceField(queryset=RangerTypes.objects.all(), label="Select Power Ranger Types")
    
