from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.IntegerField()
    difficulty = models.CharField(max_length=10)


def __str__(self):
    return self.name
