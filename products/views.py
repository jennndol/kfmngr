from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from products.models import Produk
from products.forms import ProdukForm

def produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'produk.html', {'produk':produk})

def semua_produk(request):
    semua_produk = Produk.get_semua_produk()
    return render(request, 'semua_produk.html', {'semua_produk': semua_produk})

def tambah(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            produk = Produk()
            produk.nama = form.cleaned_data.get('nama')
            produk.harga = form.cleaned_data.get('harga')
            produk.detil = form.cleaned_data.get('detil')
            produk.berat = form.cleaned_data.get('berat')
            produk.stok = form.cleaned_data.get('stok')
            produk.sku = form.cleaned_data.get('sku')
            produk.save(request.user)
            return redirect('/produk/')
    else:
        form = ProdukForm()
    return render(request, 'tambah_produk.html', {'form': form})
