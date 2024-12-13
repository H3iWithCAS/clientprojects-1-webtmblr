from django.db import models

class Tumbler(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
