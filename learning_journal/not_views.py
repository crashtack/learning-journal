from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer='stirng')
def my_view(request):
    import_text = open(os.path.join(HERE, 'sample.html')).read()
