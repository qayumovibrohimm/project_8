from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return self.name
