from django.db import models

class Tumbler(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/images/')
    description = models.TextField(blank=True)
    is_promo = models.BooleanField(default=False)  # Field promo
    is_recommended = models.BooleanField(default=False)  # Field untuk rekomendasi produk
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return self.name
    
class Meta:
    ordering = ['price']
    
class Promo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/') 
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 