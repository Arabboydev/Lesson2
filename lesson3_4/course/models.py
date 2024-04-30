from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    kurs_vaqti = models.CharField(max_length=255)
    course_type = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name

