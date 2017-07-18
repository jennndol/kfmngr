from django.db import models

class Product(models.Model):
    """docstring for Product."""
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    detail = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)
    sku = models.CharField(blank=True, null=True, max_length=10)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

    def save(self, *args, **kwargs):
        # TODO: create history if product is created
        print('save method is being called')
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    def get_stock_amount(self):
        return str(self.stock) + " Kg"

    @staticmethod
    def get_all_products():
        return Product.objects.all()

# TODO: price by weight
class PriceTag(models.Model):
    product = models.ForeignKey(Product)
    weight = models.IntegerField(default=0)
    sku = models.CharField(blank=True, null=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        pass
