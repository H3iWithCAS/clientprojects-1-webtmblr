from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),  # Beranda (halaman utama)
    path('pencarian/', views.pencarian, name='pencarian'),  # Halaman pencarian
    path('kategori/', views.kategori, name='kategori'),  # Halaman kategori
    path('rekomendasi/', views.rekomendasi, name='rekomendasi'),  # Halaman rekomendasi
    path('product/<int:id>/', views.product_detail, name='product_detail'), # URL untuk detail product
    path('', views.tumbler_list, name='tumbler_list'), # URL untuk list tumbler
    path('tumbler/<int:pk>/', views.tumbler_detail, name='tumbler_detail'), # URL untuk detail tumbler
    path('promo/', views.promo, name='promo'),  # Halaman promo
    path('promo/<int:id>/', views.promo_detail, name='promo_detail'), # URL untuk detail promo
    path('keunggulan/', views.keunggulan, name='keunggulan'),  # Halaman keunggulan  
]
