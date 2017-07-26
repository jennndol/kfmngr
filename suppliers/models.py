from django.db import models

class Pemasok(models.Model):
    """docstring for Supplier."""
    nama = models.CharField(max_length=50)
    hp = models.CharField(max_length=16)
    alamat = models.CharField(max_length=50)
    dibuat_pada = models.DateTimeField(auto_now_add = True, auto_now = False)
    diubah_pada = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name_plural = 'list pemasok'

    def __str__(self):
        return self.nama
