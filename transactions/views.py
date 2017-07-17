from django.shortcuts import render
from transactions.models import Procurement
from transactions.forms import ProcurementForm

def buying(request):
    procurements = Procurement.objects.all()
    return render(request, 'buying.html', {'procurements':procurements})

def new_buying(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid()
        procurement = Procurement()
        procurement.product = form.cleaned_data.get('product')
        procurement.supplier = form.cleaned_data.get('supplier')
        procurement.quantity = form.cleaned_data.get('quantity')
        procurement.price = form.cleaned_data.get('price')
        procurement.user = request.user
        procurement.save()
        return redirect('/buying/')

    else:
        form = ProcurementForm()
    return render(request, 'new_procurement.html', {'form':form})
