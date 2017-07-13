from django import forms

from products.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    detail = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=500)
    weight = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)

    class Meta:
        model = Product
        fields = ['name', 'price', 'detail', 'sku', 'weight', 'stock']
