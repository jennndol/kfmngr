from django import forms

from .models import Pengadaan, Penjualan, DetilPenjualan


class PengadaanForm(forms.ModelForm):

    class Meta:
        model = Pengadaan
        fields = ['produk', 'pemasok', 'kuantitas', 'harga']

class PenjualanForm(forms.ModelForm):
    class Meta:
        model = Penjualan
        fields = ['pembeli']

class DetilPenjualanForm(forms.ModelForm):
    class Meta:
        model = DetilPenjualan
        fields = ['produk', 'kuantitas']
