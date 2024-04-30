from django.db import models

class SamsungPhone(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SamsungTap(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name