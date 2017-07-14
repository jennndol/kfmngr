from django.db import models
from suppliers.models import Supplier
from products.models import Product

class Procurement(models.Model):
    """docstring for Procurement."""
    product = models.ForeignKey(Product)
    supplier = models.ForeignKey(Supplier)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

    def save(self, *args, **kwargs):
        print("Procurement save method is being called")
        product = Product.objects.get(id=self.product.id)
        print("before update : " + str(product.stock))
        product.stock = product.stock + self.quantity
        print("after update : " + str(product.stock))
        product.save()
        # TODO: update stock in products table
        super(Procurement, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name
