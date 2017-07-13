from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from products.models import Product
from products.forms import ProductForm

def products(request):
    products = Product.get_all_products()
    return render(request, 'products.html', {'products':products})

def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product':product})

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product()
            product.name = form.cleaned_data.get('name')
            product.price = form.cleaned_data.get('price')
            product.detail = form.cleaned_data.get('detail')
            product.weight = form.cleaned_data.get('weight')
            product.stock = form.cleaned_data.get('stock')
            product.save()
            return redirect('/product/')
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form': form})
