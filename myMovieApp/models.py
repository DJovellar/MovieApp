from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Movie(models.Model):
    name = models.CharField(max_length=50)
    release = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    cast = models.CharField(max_length=1000)

    def __unicode__(self):
        return u"%s" % self.name

    def averageRating(self):
        reviewCount = self.review_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.review_set.all()])
            return ratingSum / reviewCount

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.pk})

class Review(models.Model):
    #RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    #rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=4000)

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.movie.pk})
