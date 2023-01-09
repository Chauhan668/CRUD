from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField (max_length=100)
    password = models.CharField(max_length=100)

