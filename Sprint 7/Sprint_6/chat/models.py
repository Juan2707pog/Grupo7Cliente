from django.db import models

# Create your models here.

class chatnombres(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)