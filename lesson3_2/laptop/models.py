from django.db import models

class Laptop(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.TextField()
    year = models.IntegerField()
    color = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.model

class LaptopApple(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.TextField()
    year = models.IntegerField()
    color = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.model
