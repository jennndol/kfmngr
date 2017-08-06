"""kfmngr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
<<<<<<< HEAD
from products.views import semua_produk, produk, tambah
from transactions.views import semua_pengadaan, tambah_pengadaan, penjualan, detil_penjualan, bayar, pengadaan
=======
from products.views import semua_produk, produk, tambah, stok_managemen
from transactions.views import semua_pengadaan, tambah_pengadaan, penjualan, detil_penjualan, bayar
>>>>>>> fca3109e374868c15c0bd7c69a98a3a8a9c3974e

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^produk/$', semua_produk, name='semua_produk'),
    url(r'^produk/tambah/$', tambah, name='tambah_produk'),
    url(r'^produk/(?P<id>\d+)/$', produk, name='produk'),
    url(r'^pengadaan/$', semua_pengadaan, name='semua_pengadaan'),
    url(r'^pengadaan/tambah/$', tambah_pengadaan, name='tambah_pengadaan'),
    url(r'^pengadaan/(?P<id>\d+)/$', pengadaan, name='pengadaan'),
    url(r'^penjualan/$', penjualan, name='penjualan'),
    url(r'^penjualan/(?P<id>\d+)/$', detil_penjualan, name='detil_penjualan'),
    url(r'^penjualan/(?P<id>\d+)/bayar/$', bayar, name='bayar'),
    url(r'^stok/$', stok_managemen),
]
