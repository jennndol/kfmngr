from django.db import models
from suppliers.models import Supplier
from products.models import Product

class Buying(models.Model):
    """docstring for Buying."""
    supplier = models.ForeignKey(Supplier)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.id

    # TODO: Create transaction between Buying and Product
