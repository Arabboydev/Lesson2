from django.db import models

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    price = models.TextField(max_length=50)
    davomiyligi = models.TextField(max_length=255)

    def __str__(self):
        return self.course_name

class CourseAbout(models.Model):
    course_name = models.CharField(max_length=255)
    course_levels = models.IntegerField()

    def __str__(self):
        return self.course_name


