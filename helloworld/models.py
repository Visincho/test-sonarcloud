from django.db import models

# Create your models here.
class Hello(models.Model):

    title = models.CharField(max_length=256)