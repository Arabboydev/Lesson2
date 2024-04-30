from django.db import models


class TvAbout(models.Model):
    tv_name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.TextField(max_length=50)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.tv_name

class ManitorAbout(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    price = models.TextField()
    size = models.TextField()

    def __str__(self):
        return self.name

