from behave import *

"""@given(u'Exists movies registered')
def step_impl(context):
    context.browser.visit(context.get_url('myrestaurants:movie_list'))
"""
@when(u'I list movies')
def step_impl(context):
    context.browser.visit(context.get_url('myMovieApp:movie_list'))

@then(u'I´m viewing a list containing')
def step_impl(context):
    movie_links = context.browser.find_by_css('div#content ul li a')
    for i, row in enumerate(context.table):
        assert row['name'] == movie_links[i].text

@then(u'The list contains 10 movies')
def step_impl(context):
    assert count == len(context.browser.find_by_css('div#content ul li a'))
