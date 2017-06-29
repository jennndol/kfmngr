from django.db import models

class Supplier(models.Model):
    """docstring for Supplier."""
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=50)
    
    def __init__(self, arg):
        super(Supplier, self).__init__()
        self.arg = arg
