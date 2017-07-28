from django import forms

from .models import Pengadaan, DetilPengadaan, Penjualan, DetilPenjualan


class PengadaanForm(forms.ModelForm):
    class Meta:
        model = Pengadaan
        fields = ['pemasok']

class DetilPengadaanForm(forms.ModelForm):
    class Meta:
        model = DetilPengadaan
        fields = ['produk', 'kuantitas', 'harga']

class PenjualanForm(forms.ModelForm):
    class Meta:
        model = Penjualan
        fields = ['pembeli']

class DetilPenjualanForm(forms.ModelForm):
    class Meta:
        model = DetilPenjualan
        fields = ['produk', 'kuantitas']
