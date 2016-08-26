# from pyramid.response import Response
# import os
from pyramid.view import view_config
from pyramid.httpexceptions import (HTTPNotFound, HTTPFound)
# from jinja2 import Template


# HERE = os.path.dirname(__file__)

ENTRIES = [
    {
        "title": "Day 1",
        "id": 1,
        "date": "August 20, 2016",
        "body": "Today I learned about <strong>Pyramid</strong>."
    },
    {
        "title": "Day 2",
        "id": 2,
        "date": "August 21, 2016",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit</b>. Curabitur sodales ligula in libero."
    },
    {
        "title": "Day 3",
        "id": 3,
        "date": "August 22, 2016",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit</b>. Curabitur sodales ligula in libero."
    },
    {
        "title": "Day 4",
        "id": 4,
        "date": "August 23, 2016",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. <b>Lorem ipsum dolor sit amet, consectetur adipiscing elit</b>. Curabitur sodales ligula in libero."
    },
]


# TODO: stack all the @ decorators ontop off like defs


@view_config(route_name='list', renderer='templates/home.jinja2')
@view_config(route_name='create', renderer='templates/new-entry.jinja2')
def list_(request):
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='templates/single-entry.jinja2')
@view_config(route_name='update', renderer='templates/edit-entry.jinja2')
def detail(request):
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return {"entry": entry}
    else:
        raise HTTPNotFound('Entry Not Found')
