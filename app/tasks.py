import os
import logging
import requests

from celery import Celery

import settings


celery_app = Celery('tasks', broker='amqp://rabbitmq')


@celery_app.task
def delete(uuid: str):
    logging.info('Task execution started')
    requests.delete('http://fs_backend:5000' + f'/delete/{uuid}')
    logging.info(f'File {uuid} deleted')
