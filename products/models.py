from django.db import models

class Product(models.Model):
    """docstring for Product."""
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    detail = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_all_products(self):
        return Product.objects.all()
