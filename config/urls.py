from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),  # URL Admin
    path('login/', lambda request: redirect('/admin/login/'), name='login'),  # Redirect ke Admin Login
    path('', include('tumbler.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Menambahkan penanganan media