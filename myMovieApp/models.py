from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    name = models.CharField(max_length=50)
    release = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    cast = models.CharField(max_length=1000)

class Review(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, default = 1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.CharField(max_length=4000)
