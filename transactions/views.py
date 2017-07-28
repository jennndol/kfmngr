from django.shortcuts import render, redirect, get_object_or_404
from transactions.models import Pengadaan, Penjualan, DetilPenjualan
from transactions.forms import PengadaanForm, DetilPenjualanForm,PenjualanForm

def total(numbers):
    x = 0
    for number in numbers:
        x = number + x
    return x

def semua_pengadaan(request):
    semua_pengadaan = Pengadaan.objects.all()
    return render(request, 'semua_pengadaan.html', {'semua_pengadaan':semua_pengadaan})

def tambah_pengadaan(request):
    if request.method == 'POST':
        form = PengadaanForm(request.POST)
        if form.is_valid():
            pengadaan = Pengadaan()
            pengadaan.product = form.cleaned_data.get('produk')
            pengadaan.supplier = form.cleaned_data.get('pemasok')
            pengadaan.quantity = form.cleaned_data.get('kuantitas')
            pengadaan.price = form.cleaned_data.get('harga')
            pengadaan.user = request.user
            pengadaan.save()
            return redirect('/pengadaan/')

    else:
        form = PengadaanForm()
    return render(request, 'tambah_pengadaan.html', {'form':form})

# TODO: make receipt pengadaan, one receipt for many products and one supplier

def penjualan(request):
    if request.method == 'POST':
        form = PenjualanForm(request.POST)
        if form.is_valid():
            penjualan = Penjualan()
            penjualan.pembeli = form.cleaned_data.get('pembeli')
            penjualan.save()
    else:
        form = PenjualanForm()
    return render(request, 'penjualan.html', {'form':form})

def detil_penjualan(request, id):
    penjualan = get_object_or_404(Penjualan, id=id)
    keranjang = penjualan.list_produk()

    semua_subtotal = []
    for produk in keranjang:
        semua_subtotal.append(produk.subtotal())

    if request.method == 'POST':
        form = DetilPenjualanForm(request.POST)
        if form.is_valid():
            detil_penjualan = DetilPenjualan()
            detil_penjualan.penjualan = penjualan
            detil_penjualan.produk = form.cleaned_data.get('produk')
            detil_penjualan.harga_jual = detil_penjualan.produk.harga
            detil_penjualan.kuantitas = form.cleaned_data.get('kuantitas')
            detil_penjualan.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = DetilPenjualanForm()
    return render(request, 'detil_penjualan.html', {'penjualan':penjualan, 'form':form, 'total': total(semua_subtotal)})

def bayar(request, id):
    return render(request, 'bayar.html')
