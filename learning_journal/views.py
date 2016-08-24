from pyramid.response import Response
import os


HERE = os.path.dirname(__file__)


def list_(request):
    imported_text = open(os.path.join(HERE, 'templates/home.html')).read()
    return Response(imported_text)


def my_view2(request):
    imported_text = open(os.path.join(HERE, 'templates/sample2.html')).read()
    return Response(imported_text)


def create(request):
    imported_text = open(os.path.join(HERE, 'templates/new-entry.html')).read()
    return Response(imported_text)


def detail(request):
    imported_text = open(os.path.join(HERE, 'templates/single-entry.html')).read()
    return Response(imported_text)


def update(request):
    imported_text = open(os.path.join(HERE, 'templates/edit-entry.html')).read()
    return Response(imported_text)


def bootstrap(request):
    imported_text = open(os.path.join(HERE,
                                      'navbar-static-top/index.html')).read()
    return Response(imported_text)


def single_entry():
    pass


def edit_entry():
    pass


def includeme(config):
    config.add_view(list_, route_name='list')
    config.add_view(detail, route_name='detail')
    config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')

    config.add_view(bootstrap, route_name='bootstrap')
