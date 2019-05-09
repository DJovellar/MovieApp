
import operator
from functools import reduce
from behave import *
from django.db.models import Q

use_step_matcher("parse")

@given(u'Exists movies registered')
def step_impl(context):
    from myMovieApp.models import Movie
    for row in context.table:
        movie = Movie(release=1999)
        for heading in row.headings:
            setattr(movie, heading, row[heading])
        movie.save()

@when(u'I list movies')
def step_impl(context):
    context.browser.visit(context.get_url('movies_list'))

@then(u'I´m viewing a list containing')
def step_impl(context):
    movie_links = context.browser.find_by_css('div#content ul li a')
    for i, row in list(enumerate(context.table)):
        print(movie_links[i].text)
        print(row['name'])
        assert row['name'] == movie_links[i].text

@then(u'The list contains 10 movies')
def step_impl(context):
    assert 10 == len(context.browser.find_by_css('div#content ul li a'))
