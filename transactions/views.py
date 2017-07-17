from django.shortcuts import render
from transactions.models import Procurement

def buying(request):
    procurements = Procurement.objects.all()
    return render(request, 'buying.html', {'procurements':procurements})

def new_buying(request):
    return render(request, 'new_procurement.html')
