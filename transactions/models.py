from django.db import models
from suppliers.models import Supplier
from products.models import Product
from django.contrib.auth.models import User
from notifications.models import History

class Procurement(models.Model):
    """docstring for Procurement."""
    product = models.ForeignKey(Product)
    supplier = models.ForeignKey(Supplier)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)
    user = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        print("Procurement save method is being called")
        product = Product.objects.get(id=self.product.id)
        print("before update : " + str(product.stock))
        product.stock = product.stock + self.quantity
        print("after update : " + str(product.stock))
        history = History.create('%s added %s Kg of %s that is sent by %s' % (self.user, self.quantity, self.product, self.supplier))
        history.save()
        product.save()
        super(Procurement, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name

class Selling(models.Model):
    buyer = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '#' + str(self.pk) + ' - '+ self.buyer

class Detail(models.Model):
    selling = models.ForeignKey(Selling)
    product = models.ForeignKey(Product, related_name='+')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.quantity * self.product.price
