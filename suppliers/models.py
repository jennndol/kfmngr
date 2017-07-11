from django.db import models

class Supplier(models.Model):
    """docstring for Supplier."""
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return self.name
