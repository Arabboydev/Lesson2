from django.db import models


class GameComputer(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ComputerX(models.Model):
    name = models.CharField(max_length=255)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    xotira = models.CharField(max_length=255)

    def __str__(self):
        return self.name