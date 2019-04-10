from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=50)
    release = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    cast = models.CharField(max_length=1000)

class Review(models.Model):
    movie = ForeignKey(Movie, on_delete=models.CASCADE)
    user = ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerRangeField(null = False, min_value=1, max_value=10)
    description = models.CharField(max_length=4000)
