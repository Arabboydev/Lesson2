from django.db import models

class IphonePhone(models.Model):
    phone_name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_name

class AppleAirPods(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name