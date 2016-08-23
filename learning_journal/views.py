from pyramid.response import Response
import os


HERE = os.path.dirname(__file__)


def my_view(request):
    imported_text = open(os.path.join(HERE, 'sample.html')).read()
    return Response(imported_text)


def my_view2(request):
    imported_text = open(os.path.join(HERE, 'sample2.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(my_view, route_name='home')
    config.add_view(my_view2, route_name='detail')
