from django.db import models
from django.db.models.deletion import CASCADE
from info1.models import Infoinsta

# Create your models here.

class chatnombres(models.Model):
    first_name = models.CharField(max_length=128, primary_key=True)
    last_name = models.CharField(max_length=128)
    asd = models.ForeignKey(Infoinsta, on_delete=CASCADE)