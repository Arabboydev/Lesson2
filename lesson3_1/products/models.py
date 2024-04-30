from django.db import models


class Cars(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.model


class ElekroMobil(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    power = models.CharField(max_length=255)

    def __str__(self):
        return self.model
