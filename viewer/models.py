from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)