from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm

def buying(request):
    products = Product.get_all_products()
    return render(request, 'buying.html', {'products':products})
