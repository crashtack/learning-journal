from pyramid.response import Response
import os
from pyramid.view import view_config
# from jinja2 import Template



HERE = os.path.dirname(__file__)

ENTRIES = [
     {
        "title": "Day1",
        "id": 1,
        "date": "August 20, 2016",
        "body": "Today I learned about <strong>Pyramid</strong>."
     },
     {
        "title": "Day2",
        "id": 2,
        "date": "August 21, 2016",
        "body": "Today I learned about heaps and templates."
     },
     {
        "title": "Day3",
        "id": 3,
        "date": "August 22, 2016",
        "body": "Today I learned about deque."
     },
     {
        "title": "Day4",
        "id": 4,
        "date": "August 23, 2016",
        "body": "Today I learned about queue."
     },
]


@view_config(route_name='list', renderer='templates/home.jinja2')
def list_(request):
    # imported_text = open(os.path.join(HERE, 'templates/home.html')).read()
    return {"entries": ENTRIES}


@view_config(route_name='create', renderer='templates/new-entry.jinja2')
def create(request):
    # imported_text = open(os.path.join(HERE, 'templates/new-entry.html')).read()
    return {"entries": ENTRIES}


def detail(request):
    imported_text = open(os.path.join(HERE, 'templates/single-entry.html')).read()
    return Response(imported_text)


def update(request):
    imported_text = open(os.path.join(HERE, 'templates/edit-entry.html')).read()
    return Response(imported_text)


def my_view2(request):
    imported_text = open(os.path.join(HERE, 'templates/sample2.html')).read()
    return Response(imported_text)


@view_config(route_name='bootstrap', renderer='navbar-static-top/index.jinja2')
def bootstrap(request):
    imported_text = open(os.path.join(HERE,
                                      'navbar-static-top/index.html')).read()
    return Response(imported_text)


# @view_config(route_name='list', renderer='templates/home.jinja2')
# def bootstrap1(request):
#     imported_text = open(os.path.join(HERE,
#                                       'navbar-static-top/index.html')).read()
#     return Response(imported_text)


def includeme(config):
    # config.add_view(list_, route_name='list')
    config.add_view(detail, route_name='detail')
    # config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')

    config.add_view(bootstrap, route_name='bootstrap')
