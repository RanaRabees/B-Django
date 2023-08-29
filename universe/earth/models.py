from distutils.command.upload import upload
import email
from email.policy import default
from unicodedata import name
from django.db import models
from matplotlib import image


# Create your models here.
class Membership(models.Model):
    person = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    invite_reason = models.CharField(max_length=64)
    images = models.ImageField(upload_to = "images" ,default="")


    def __str__(self):
        return self.person





class info(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.name