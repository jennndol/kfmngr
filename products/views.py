from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def products(request):
    # FIXME: adding template
    products = Product.get_all_products()
    return HttpResponse(products, content_type="text/plain")
