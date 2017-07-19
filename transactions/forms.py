from django import forms

from .models import Procurement, Selling


class ProcurementForm(forms.ModelForm):

    class Meta:
        model = Procurement
        fields = ['product', 'supplier', 'quantity', 'price']

class SellingForm(forms.ModelForm):
    class Meta:
        model = Selling
        fields = ['buyer']
