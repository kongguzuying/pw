from django.db import models

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
