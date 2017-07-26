from django.db import models

# TODO: product's price is separated by packing
class Produk(models.Model):
    """docstring for Product."""
    nama = models.CharField(max_length=100)
    harga = models.IntegerField(default=0)
    detil = models.CharField(max_length=100)
    berat = models.IntegerField(default=0)
    sku = models.CharField(blank=True, null=True, max_length=10)
    stok = models.IntegerField(default=0)
    dibuat_pada = models.DateTimeField(auto_now_add = True, auto_now = False)
    dibuat_pada = models.DateTimeField(auto_now_add = False, auto_now = True)

    def save(self, *args, **kwargs):
        # TODO: create history if product is created
        print('save method is being called')
        super(Produk, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.nama)

    def get_jumlah_stok(self):
        return str(self.stok) + " Kg"

    @staticmethod
    def get_semua_produk():
        return Produk.objects.all()
