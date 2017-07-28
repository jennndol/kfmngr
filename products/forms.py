from django import forms

from products.models import Produk

class ProdukForm(forms.ModelForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    harga = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    berat = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    stok = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Produk
        fields = ['nama', 'harga', 'berat', 'stok']
