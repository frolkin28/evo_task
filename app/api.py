from flask import Blueprint, request, send_file, jsonify

import settings

from app.services import FileService
from app.exceptions import FileExpired

api_bp = Blueprint('api', __name__)


@api_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file', None)
    ttl = request.form.get('ttl', None)
    if not file or not ttl:
        return '', 400
    else:
        if not file.filename:
            return '', 400
        url = FileService().upload(file, ttl)
        if not url:
            return '', 400
        response = {'url': url}
        return jsonify(response), 201


@api_bp.route('/download/<uuid>', methods=['GET'])
def download(uuid):
    try:
        path, name = FileService().download(uuid)
        return send_file(path, attachment_filename=name, as_attachment=True)
    except (FileNotFoundError, FileExpired) as exc:
        return '', 404
