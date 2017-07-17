from django.shortcuts import render
from transactions.models import Procurement

def buying(request):
    procurements = Procurement.objects.all()
    return render(request, 'buying.html', {'procurements':procurements})
