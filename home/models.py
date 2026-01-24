from django.db import models

class DataModels(models.Model):
    name=models.CharField(max_length=50)
    salary=models.TextField()
    age=models.CharField()

# Create your models here.
