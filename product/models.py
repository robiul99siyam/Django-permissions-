from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=15,decimal_places=2,default = 00.00)

class color(models.Model):
    title = models.CharField(max_length=20)