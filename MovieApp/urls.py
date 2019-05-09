"""MovieApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django.views.generic import RedirectView
from myMovieApp.views import home_view, logged_in_view, logged_out_view, movie_view, review, LoginRequiredCheckIsOwnerUpdateView, delete_review
from django.views.generic import DetailView, ListView
from myMovieApp.models import Movie, Review
from myMovieApp.forms import ReviewForm


urlpatterns = [
    #path('', home_view, name='home'),
    #path('home/', home_view, name='home'),

    path('accounts/profile/', logged_in_view, name='loggedin'),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='loggedout'),
    path('movies/<int:pk>', movie_view.as_view(), name='movie_detail'),
    path('movies/<int:pk>/reviews/create', review, name='review_create'),
    path('movies/<int:pk>/reviews/delete', delete_review, name='review_delete'),
    path('movies/<int:pkr>/reviews/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Review,
            form_class=ReviewForm),
        name='review_edit'),
    path('movies/<int:pkr>',
        DetailView.as_view(
            model=Movie,
            template_name='myMovieApp/movie_detail.html'),
        name='movie_detail'),
    url('', ListView.as_view(
                        model=Movie,
                        queryset=Movie.objects.all(),
                        context_object_name="movies_list",
                        template_name='myMovieApp/movie_list.html'),
                        name='movies_list'),




]
