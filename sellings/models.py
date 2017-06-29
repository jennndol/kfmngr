from django.db import models
from products.models import Product

class Selling(models.Model):
    """docstring for Selling."""
    buyer = models.CharField(max_length=50)
    product = models.IntegerField(Product)
    quantity = models.IntegerField()

    def __init__(self, arg):
        super(Selling, self).__init__()
        self.arg = arg
