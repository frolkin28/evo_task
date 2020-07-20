import uuid
import re
import typing
import datetime
import os

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

import settings

from app.exceptions import FileExpired
from app.database import db
from app.models import File
from app import tasks


class FileService:
    def upload(self, file: FileStorage, ttl: str) -> typing.Optional[str]:
        original_filename = secure_filename(file.filename)
        filename, extention = self.validate_filename(original_filename)
        if not (filename and extention):
            return None
        else:
            uuid, filename = self.generate_unique_name(filename, extention)
            path = settings.UPLOADS_DIR / filename
            ttl = datetime.datetime.strptime(ttl, "%Y/%m/%d %H:%M")

            file.save(path)
            db.session.add(File(str(path), original_filename, ttl, uuid))
            db.session.commit()

            tasks.delete.apply_async(args=[uuid], eta=(ttl - datetime.timedelta(hours=3)))
            url = '{}/{}/{}'.format(settings.DOMAIN, 'download', uuid)
            return url

    def download(self, uuid: str) -> typing.Tuple:
        file = db.session.query(File).filter_by(uuid=uuid).first()
        if file:
            if file.ttl > datetime.datetime.now():
                return file.path, file.name
            else:
                raise FileExpired
        else:
            raise FileNotFoundError

    def get_file(self, uuid: str) -> File:
        file = db.session.query(File).filter_by(uuid=uuid).first()
        return file

    def delete_file(self, uuid: str) -> None:
        file = db.session.query(File).filter_by(uuid=uuid).first()
        if not file:
            return
        else:
            os.remove(file.path)
            db.session.delete(file)
            db.session.commit()

    @staticmethod
    def validate_filename(filename: str) -> typing.Optional[typing.Tuple]:
        pattern = re.compile(r'(.+)\.(.+)')
        result = re.search(pattern, filename)
        if not result:
            return None, None
        else:
            filename = result.group(1)
            extention = result.group(2)
            return filename, extention

    @staticmethod
    def generate_unique_name(filename: str, extention: str) -> typing.Optional[typing.Tuple]:
        file_uuid = str(uuid.uuid4())
        if len(filename) > 5:
            filename = filename[:5]
        filename = '{}-{}.{}'.format(filename, file_uuid[:18], extention)
        return file_uuid, filename
