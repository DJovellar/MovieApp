from django.forms import ModelForm
from myMovieApp.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'movie',)
