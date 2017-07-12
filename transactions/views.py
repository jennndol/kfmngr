from django.shortcuts import render
from products.models import Product
from products.forms import ProductForm

def buying(request):
    products = Product.get_all_products()
    return render(request, 'buying.html', {'products':products})


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
            return redirect('/transaction/')
    else:
        form = ArticleForm()
    return render(request, 'create.html', {'form': form})
