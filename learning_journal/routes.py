def includeme(config):
    config.add_route('list', '/')
    config.add_route('create', '/journal/new-entry')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')
    config.add_route('bootstrap', '/bootstrap/')
    config.add_route('bootstrap_navbar', '/bootnav')
    config.add_route('bootstrap_navbar2', '/bootnav/')
    config.add_static_view('static', 'static', cache_max_age=3600)
