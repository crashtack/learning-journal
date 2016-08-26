def includeme(config):
    config.add_route('list', '/')
    config.add_route('create', '/journal/new-entry')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')
