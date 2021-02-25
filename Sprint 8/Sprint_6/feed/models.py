from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=128, primary_key=True)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)