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
    return {"entries": ENTRIES}


@view_config(route_name='create', renderer='templates/new-entry.jinja2')
def create(request):
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='templates/single-entry.jinja2')
def detail(request):
    return {"entries": ENTRIES}


@view_config(route_name='update', renderer='templates/edit-entry.jinja2')
def update(request):
    return {"entries": ENTRIES}


@view_config(route_name='bootstrap', renderer='templates/bootstrap.jinja2')
def bootstrap(request):
    return {"entries": ENTRIES}


@view_config(route_name='bootstrap_navbar', renderer='navbar-static-top/index.jinja2')
def bootstrap_navbar(request):
    return {"entries": ENTRIES}


@view_config(route_name='bootstrap_navbar2', renderer='navbar-static-top/index.jinja2')
def bootstrap_navbar2(request):
    return {"entries": ENTRIES}
