from flask import Blueprint, render_template

import settings

main = Blueprint(
    'main',
    __name__,
    template_folder=str(settings.BASE_DIR / 'app' / 'template'),
    static_folder=str(settings.BASE_DIR / 'app' / 'static')
)


@main.route('/')
def home():
    return render_template('index.html')