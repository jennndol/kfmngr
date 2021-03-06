from django.db import models
from suppliers.models import Pemasok
from products.models import Produk
from django.contrib.auth.models import User
from notifications.models import History
from django.contrib.humanize.templatetags.humanize import naturaltime

class Pengadaan(models.Model):
    pemasok = models.ForeignKey(Pemasok)
    dibuat_pada = models.DateTimeField(auto_now_add = True, auto_now = False)
    diubah_pada = models.DateTimeField(auto_now_add = False, auto_now = True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'list pengadaan'

    def __str__(self):
        return naturaltime(self.dibuat_pada)

class DetilPengadaan(models.Model):
    """docstring for Pengadaan."""
    produk = models.ForeignKey(Produk)
    kuantitas = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)
    dibuat_pada = models.DateTimeField(auto_now_add = True, auto_now = False)
    diubah_pada = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name_plural = 'list detail pengadaan'

    def hitung_modal(self):
        return ((self.kuantitas * self.harga) + (self.produk.modal * self.produk.stok))/(self.kuantitas + self.produk.stok)

    def save(self, *args, **kwargs):
        print("Pengadaan save method is being called")
        # produk = Produk.objects.get(id=self.produk.id)
        # print("before update : " + str(produk.stok))
        # produk.modal = self.hitung_modal()
        # produk.stok = produk.stok + self.kuantitas
        # print("after update : " + str(produk.stok))
        # history = History.create('added %s Kg of %s' % (self.kuantitas, self.produk))
        # history.save()
        # produk.save()
        super(DetilPengadaan, self).save(*args, **kwargs)

    def __str__(self):
        return self.produk.nama

# TODO: make sure how to manage return products

class Penjualan(models.Model):
    SUDAH = 'SD'
    BELUM = 'BL'
    PILIHAN = (
        (SUDAH, 'Sudah dibayar'),
        (BELUM, 'Belum dibayar'),
    )
    status = models.CharField(max_length=2, choices=PILIHAN, default=BELUM)
    pembeli = models.CharField(max_length=50, blank=True, null=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True, auto_now=False)
    diubah_pada = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'list penjualan'

    def list_produk(self):
        return self.detilpenjualan_set.all()

    def __str__(self):
        return '#' + str(self.pk) + ' - '+ self.pembeli

class DetilPenjualan(models.Model):
    penjualan = models.ForeignKey(Penjualan)
    produk = models.ForeignKey(Produk, related_name='+')
    harga_jual = models.IntegerField(default=0)
    kuantitas = models.IntegerField()
    laba = models.IntegerField(default=0)
    dibuat_pada = models.DateTimeField(auto_now_add=True, auto_now=False)
    diubah_pada = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'list detil penjualan'

    def __str__(self):
        return self.produk.nama

    def subtotal(self):
        return self.kuantitas * self.harga_jual

    def save(self, *args, **kwargs):
        self.harga_jual = self.produk.harga
        self.laba = (self.produk.harga - self.produk.modal) * self.kuantitas
        super(DetilPenjualan, self).save(*args, **kwargs)
