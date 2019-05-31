#!/usr/bin/env python
# MUST DO: $ export DJANGO_SETTINGS_MODULE="MovieApp.settings"
import os
import json
import django
import time
import requests
import urllib.request
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieApp.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "MovieApp.settings"

django.setup()
from myMovieApp.models import Movie

def get_trailer(movie_name):
    query = urllib.parse.quote(movie_name + " trailer")
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        id = vid['href'].split("=")[1]
        return ('https://www.youtube.com/embed/' + id)

movie_prefixes = ["the dark", "godfather", "inception", "matrix", "hobbit", "lord", "seven", "interstellar", "la", "american", "whiplash", "spiderman", "gladiator", "apocalypse", "aliens", "coco"]
print("About to load a couple movies from API into database...")

for prefix in movie_prefixes:
    movie = requests.get('http://www.omdbapi.com/?apikey=8c61d702&t=' + prefix)
    parsed_movie = movie.json()
    movie_name = parsed_movie.get("Title")
    print("Inserting: " + movie_name)
    movie_release = int((parsed_movie.get("Year")).split("–")[0])
    movie_genre = parsed_movie.get("Genre")
    movie_director = parsed_movie.get("Director")
    movie_duration = parsed_movie.get("Runtime")
    movie_cast = parsed_movie.get("Actors")
    movie_country = parsed_movie.get("Country")
    movie_description = parsed_movie.get("Plot")
    movie_trailer = get_trailer(movie_name)
    m = Movie(name = movie_name,
              release = movie_release,
              genre = movie_genre,
              description = movie_description,
              duration = movie_duration,
              director = movie_director,
              country = movie_country,
              cast = movie_cast,
              trailer = movie_trailer)
    m.save()
