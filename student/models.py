import uuid
from django.db import models


class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)


    def __str__(self):

        return self.name