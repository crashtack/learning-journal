from pyramid.response import Response
import os


HERE = os.path.dirname(__file__)


def my_view(request):
    imported_text = open(os.path.join(HERE, 'template/sample.html')).read()
    return Response(imported_text)


def my_view2(request):
    imported_text = open(os.path.join(HERE, 'sample2.html')).read()
    return Response(imported_text)


def journal(request):
    imported_text = open(os.path.join(HERE, 'journal.html')).read()
    return Response(imported_text)


def new_entry(request):
    imported_text = open(os.path.join(HERE, 'journal.html')).read()
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
    config.add_view(my_view, route_name='home')
    config.add_view(my_view2, route_name='detail')
    config.add_view(journal, route_name='journal')
    config.add_view(new_entry, route_name='new-entry')
    config.add_view(single_entry, route_name='single-entry')
    config.add_view(edit_entry, route_name='edit-entry')

    config.add_view(bootstrap, route_name='bootstrap')
