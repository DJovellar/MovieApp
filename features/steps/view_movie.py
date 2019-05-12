from behave import *

use_step_matcher("parse")


@given(u'Exists a user “{username}” with password “{password}”')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)


@given(u'Exists a movie')
def step_impl(context):
    from myMovieApp.models import Movie
    movie = Movie()
    for row in context.table:
        for heading in row.headings:
            setattr(movie, heading, row[heading])
    movie.save()


@given(u'Exists a review at movie “{movie_name}” by “{username}”')
def step_impl(context, movie_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from myMovieApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    from myMovieApp.models import Review
    for row in context.table:
        review = Review(movie=movie, user=user)
        for heading in row.headings:
            setattr(review, heading, row[heading])
        review.save()


@given(u'I view the details for movie “{movie_name}”')
def step_impl(context, movie_name):
    from myMovieApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    context.browser.visit(context.get_url('movie_detail', movie.pk))


@then(u'I\'m viewing movie details including')
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])


@then(u'I\'m viewing a movie reviews list containing')
def step_impl(context):
    review_par_links = context.browser.find_by_css('div#content ul li p')
    for i, row in enumerate(context.table):
        print(review_par_links[3*i].text)
        print(review_par_links[3*i+1].text)
        assert review_par_links[3*i].text.startswith(row['rating'])
        assert row['description'] == review_par_links[3*i+1].text
        assert review_par_links[3*i+2].text.startswith('Created by '+row['user'])


@then(u'The list contains {count:n} reviews')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li p')) / 3
