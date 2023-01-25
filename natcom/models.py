from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)
    credit = models.IntegerField()
    desc = models.TextField()

