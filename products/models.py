from django.db import models

class Product(models.Model):
    """docstring for Product."""
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __init__(self, arg):
        super(Product, self).__init__()
        self.arg = arg
