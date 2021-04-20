from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)