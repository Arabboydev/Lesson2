from django.db import models

class Mentor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    tajribasi = models.CharField(max_length=255)
    level = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


