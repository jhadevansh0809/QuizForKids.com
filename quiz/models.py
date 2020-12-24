from django.db import models
from django.urls import reverse

# Create your models here.


class Question(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)

    def ans(self):
        return answer

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('home')