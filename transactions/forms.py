from django import forms

from .models import Procurement


class ProcurementForm(forms.ModelForm):
    
    class Meta:
        model = Procurement
        fields = ['product', 'supplier', 'quantity', 'price']
