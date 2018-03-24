# -*- encoding: utf-8 -*-

from pathlib import Path

from emoji.routes import emoji
from emoji.routes.api import fonts
from emoji.routes.views import index


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/emoji', emoji.generate)
    app.router.add_get('/api/fonts', fonts.all)
    app.router.add_get('/api/v1/fonts', fonts.all_v1)
    _setup_static_routes(app)


def _setup_static_routes(app):
    app.router.add_static(
        '/static',
        str(Path(app['config']['project_path']).joinpath('public')),
        name='static',
        append_version=True,
    )


if __name__ == '__main__':
    pass
