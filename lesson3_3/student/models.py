from django.db import models

class StudentPage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    specialty = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.first_name} { self.last_name}"

class IqtidorliTalaba(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    xorijiy_til = models.CharField(max_length=255)
    dasturlash_mahorati = models.CharField(max_length=255)
    GPA = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} { self.last_name}"