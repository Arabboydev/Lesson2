from django.db import models

class IeltsCenterabout(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255, blank=True, null=True)
    experiment = models.IntegerField()

    def __str__(self):
        return self.name


class IeltsCoursesAbout(models.Model):
    course_name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.course_name