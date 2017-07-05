from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def products(request):
    return render(request, 'products.html')

def Product(request):
    # TODO: show product by id
    product = Product.objects.filter(id=id)
    return HttpResponse(product, content_type="text/plain")
