from django.db import models

class AirConsider(models.Model):
    conditioner_name = models.CharField(max_length=255)
    make = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.conditioner_name


class WashingMachine(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    capacity = models.TextField()

    def __str__(self):
        return self.name