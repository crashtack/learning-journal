def includeme(config):
    config.add_route('home', '/')
    config.add_route('detail', '/detail/')
    config.add_route('journal', '/journal/')
    config.add_route('bootstrap', '/bootstrap/')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_static_view('special_styles', 'special_styles', cache_max_age=3600)
    # config.add_static_view('misc_styles', 'misc_styles', cache_max_age=3600)
