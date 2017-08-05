from django.db import models

# TODO: product's price is separated by packing
class Produk(models.Model):
    """docstring for Product."""
    nama = models.CharField(max_length=100)
    modal = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)
    berat = models.IntegerField(default=0)
    stok = models.IntegerField(default=0)
    dibuat_pada = models.DateTimeField(auto_now_add = True, auto_now = False)
    dibuat_pada = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name_plural = 'list produk'

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

class BeratLiter(models.Model):
    produk = models.ForeignKey(Produk)
    berat = models.IntegerField(default=0)

    def __str__(self):
        return self.produk.nama
