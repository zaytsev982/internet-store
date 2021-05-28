from django.db import models

# Create your models here.


class Employee:
    def __init__(self, name, age, gender, second_name):
        self.name = name
        self.age = age
        self.gender = gender
        self.second_name = second_name

        # self.name = models.CharField(max_length=20)
        # self.age = models.IntegerField()
        # self.gender = models.CharField(max_length=10)
        # self.second_name = models.CharField(max_length=20)