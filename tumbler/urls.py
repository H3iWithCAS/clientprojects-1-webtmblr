from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.beranda, name='beranda'),  # Beranda (halaman utama)
    path('pencarian/', views.pencarian, name='pencarian'),  # Halaman pencarian
    path('kategori/', views.kategori, name='kategori'),  # Halaman kategori
    path('rekomendasi/', views.rekomendasi, name='rekomendasi'),  # Halaman rekomendasi
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('promo/', views.promo, name='promo'),  # Halaman promo
    path('promo/<int:id>/', views.promo_detail, name='promo_detail'),
    path('keunggulan/', views.keunggulan, name='keunggulan'),  # Halaman keunggulan  
    path('', views.tumbler_list, name='tumbler_list'),
    path('tumbler/<int:pk>/', views.tumbler_detail, name='tumbler_detail'),
    path('tumbler/new/', views.tumbler_create, name='tumbler_create'),
    path('tumbler/<int:pk>/edit/', views.tumbler_edit, name='tumbler_edit'),
    path('tumbler/<int:pk>/delete/', views.tumbler_delete, name='tumbler_delete'),
    # URL untuk login
    path('login/', CustomLoginView.as_view(), name='login'),
]
