from django.shortcuts import render
from products.models import Product

def buying(request):
    products = Product.get_all_products()
    return render(request, 'buying.html', {'products':products})
