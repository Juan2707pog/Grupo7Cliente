from django.db import models

# Create your models here.

class Infoinsta(models.Model):
    nick_name = models.CharField(max_length=128, primary_key=True)
    arroba = models.CharField(max_length=128)
    biography = models.CharField(max_length=128)
    followers = models.CharField(max_length=128)
    followeds = models.CharField(max_length=128)
    publications = models.CharField(max_length=128)
    url = models.CharField(max_length=128)