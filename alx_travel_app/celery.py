from __future__ import absolute_import, unicode_literals
import os


class Celery:
    def autodiscover_tasks(self):
        pass

    def config_from_object(self, param, namespace):
        pass


from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery()

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
