from django.contrib import admin
from .models import Tumbler

@admin.register(Tumbler)
class TumblerAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price')  # Tambahkan 'price' ke daftar kolom
    list_filter = ('price',)

