from flask import Blueprint, request, send_from_directory

import settings

api_bp = Blueprint('api', __name__)


@api_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file', None)
    if not file:
        return 404
    else:
        if not file.filename:
            return 404
        file.save(settings.UPLOADS_DIR / file.filename)
    return "", 201


@api_bp.route('/download/<filename>', methods=['GET'])
def download(filename):
    try:
        return send_from_directory(settings.UPLOADS_DIR, filename=filename, as_attachment=True)
    except FileNotFoundError:
        return '', 404