from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField

# Create your models here.

class User(models.Model):

    usuario = models.CharField(max_length=50)
    contra = models.CharField(max_length=50)
    contra2 = models.CharField(max_length=50)
    email = models.EmailField