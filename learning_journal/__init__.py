from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600) # not in stevens code
    # config.add_jinja2_render('.html') # from stevens code
    config.include('.routes')
    # config.include('.views')
    config.scan()
    return config.make_wsgi_app()
