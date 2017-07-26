from django.test import TestCase

from .models import Produk

class ProdukModelTests(TestCase):
    def test_get_semua_produk(self):
        semua_produk_1 = Produk.objects.all()
        semua_produk_2 = Produk.get_semua_produk()
        if semua_produk_1.count() == 0:
            print("There's no record inside the table")
        else:
            self.assertEqual(semua_produk_1, semua_produk_2)
