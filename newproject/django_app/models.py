from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=123)
    summary = models.TextField(blank=True, null=False)
    feature = models.BooleanField(default=True)