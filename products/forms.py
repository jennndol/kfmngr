from django import forms

from products.models import Produk

class ProdukForm(forms.ModelForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    harga = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    detil = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=500)
    berat = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    stok = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)

    class Meta:
        model = Produk
        fields = ['nama', 'harga', 'detil', 'sku', 'berat', 'stok']
