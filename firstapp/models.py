from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    second_name = models.CharField(max_length=20)