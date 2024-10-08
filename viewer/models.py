from django.db import models

# Create your models here.

class CarFeature(models.Model):
    feature_name = models.CharField(max_length=30)
    def __str__(self):
        return f"Featura {self.feature_name}"

class Car(models.Model):
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    features = models.ManyToManyField(CarFeature)

    def __str__(self):
        return f"Značka {self.brand} Barva {self.color}"

class Offer(models.Model):
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    offered_car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Nabídka {self.offered_car.brand} - {self.price} EUR"





class Comment(models.Model):
    text = models.CharField(max_length=128)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)