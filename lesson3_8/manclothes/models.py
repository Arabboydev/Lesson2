from django.db import models

class Shoes(models.Model):
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.make


class T_Shirt(models.Model):
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.make