from django.db import models

class employee(models.Model):
    Name=models.CharField(max_length=50)
    Pin=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
