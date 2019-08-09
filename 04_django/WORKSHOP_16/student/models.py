from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'