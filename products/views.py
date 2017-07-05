from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def products(request):
    products = Product.get_all_products()
    return render(request, 'products.html', {'products':products})
