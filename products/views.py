from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from products.models import Product

def products(request):
    products = Product.get_all_products()
    return render(request, 'products.html', {'products':products})

def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product':product})
