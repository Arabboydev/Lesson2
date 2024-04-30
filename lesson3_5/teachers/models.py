from django.db import models

class Teachers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    ielts_level = models.IntegerField()
    experiment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeacherAbout(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    region = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
