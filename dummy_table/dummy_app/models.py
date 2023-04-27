from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
