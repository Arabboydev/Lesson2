from django.db import models

class TeacherPage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    speciality = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FahirliUstoz(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    ilmiy_unvoni = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    yonalish = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
