from django.db import models

# Create your models here.


class Hello(models.Model):

    title = models.CharField(max_length=256)


class World(models.Model):
    title = models.CharField(max_length=256)
    hello = models.ForeignKey(Hello, on_delete=models.CASCADE)
