from django.contrib import admin
from .models import Procurement, Selling, Detail

admin.site.register(Procurement)
admin.site.register(Selling)
admin.site.register(Detail)
