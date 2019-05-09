from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from myMovieApp.models import Movie, Review

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "myMovieApp/movie_list.html", {})

def logged_in_view(request, *args, **kwargs):
    return render(request, "myMovieApp/logged_in.html", {})

def logged_out_view(request, *args, **kwargs):
    return render(request, "myMovieApp/logged_out.html", {})

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'myMovieApp/form_delete.html'
    success_url = reverse_lazy('movie_detail', kwargs={'pk': 'get_object.movie.pk'})

    def get_object(self, *args, **kwargs):
        obj = super(ReviewDelete, self).get_object(*args, **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'myMovieApp/form.html'

class movie_view(DetailView):
    model = Movie
    template_name = 'myMovieApp/movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super(movie_view, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

@login_required()
def review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if Review.objects.filter(movie=movie, user=request.user).exists():
        Review.objects.get(movie=movie, user=request.user).delete()
    new_review = Review(
        rating=request.POST['rating'],
        description=request.POST['description'],
        user=request.user,
        movie=movie)
    new_review.save()
    return HttpResponseRedirect(reverse('movie_detail', args=(movie.id,)))

@login_required()
def delete_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    Review.objects.get(movie=movie, user=request.user).delete()
    return HttpResponseRedirect(reverse('movie_detail', args=(movie.id,)))
