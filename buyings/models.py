from django.db import models
from suppliers.models import Supplier
from products.models import Product

class Buying(models.Model):
    """docstring for Buying."""
    supplier = models.ForeignKey(Supplier)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __init__(self, arg):
        super(Buying, self).__init__()
        self.arg = arg
