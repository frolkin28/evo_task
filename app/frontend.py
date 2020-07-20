from flask import Blueprint, render_template

import settings

from app.services import FileService

main = Blueprint(
    'main',
    __name__,
    template_folder=str(settings.BASE_DIR / 'app' / 'template'),
    static_folder=str(settings.BASE_DIR / 'app' / 'static')
)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/file/<uuid>')
def get_file(uuid):
    file = FileService().get_file(uuid)
    if not file:
        return render_template('404.html')
    else:
        name, ttl, uuid = file.name, file.ttl, file.uuid
        return render_template('file.html', name=name, ttl=ttl, uuid=uuid)