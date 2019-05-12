from behave import *


use_step_matcher("parse")


@when(u'I register a review at movie "{movie_name}"')
def step_impl(context, movie_name):
    from myMovieApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    for row in context.table:
        context.browser.visit(context.get_url('movie_detail', movie.pk))
        form = context.browser.find_by_tag('form').first
        context.browser.choose('rating', row['rating'])
        context.browser.fill('description', row['description'])
        form.find_by_value('Review').first.click()


@given(u'Exists a review at movie "{movie_name}" by "{username}"')
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


@when(u'I edit the current review as "{username}" for "{movie_name}"')
def step_impl(context, username, movie_name):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from myMovieApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    from myMovieApp.models import Review
    review = Review.objects.get(user=user)
    context.browser.visit(context.get_url('review_edit', movie.pk, review.pk))
    form = context.browser.find_by_tag('form').first

    if context.browser.url == context.get_url('review_edit', movie.pk, review.pk)\
            and context.browser.find_by_tag('form'):
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()



@when(u'I view the movie "{movie_name}" details')
def step_impl(context, movie_name):
    from myMovieApp.models import Movie
    movie = Movie.objects.get(name=movie_name)
    context.browser.visit(context.get_url('movie_detail', movie.pk))
