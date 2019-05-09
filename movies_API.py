#!/usr/bin/env python
# MUST DO: $ export DJANGO_SETTINGS_MODULE="MovieApp.settings"
import os
import json
import django
import time
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieApp.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "MovieApp.settings"

django.setup()

from myMovieApp.models import Movie


movie_prefixes = ["abi", "ha", "ri", "se", "the", "lord", "tom", "an", "la", "st", "pe", "joe", "li", "pa", "and", "des"]
print("About to load a couple movies from API into database...")

for prefix in movie_prefixes:
    movie = requests.get('http://www.omdbapi.com/?apikey=8c61d702&t=' + prefix)
    parsed_movie = movie.json()
    movie_name = parsed_movie.get("Title")
    print("Inserting: " + movie_name)
    movie_release = int((parsed_movie.get("Year")).split("–")[0])
    movie_genre = parsed_movie.get("Genre")
    movie_cast = parsed_movie.get("Actors")
    movie_description = parsed_movie.get("Plot")
    m = Movie(name = movie_name,
              release = movie_release,
              genre = movie_genre,
              description = movie_description,
              cast = movie_cast)
    m.save()