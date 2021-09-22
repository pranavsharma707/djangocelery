from __future__ import absolute_import,unicode_literals
from django.conf import settings
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','celeryproject.settings')
app=Celery('celeryproject')
app.config_from_object('django.conf:settings')

app.conf.beat_scheduler={
    'multiple-every-minute':{
        'task':'celeryapp.task.multiple_two_numbers',
        'schedule':10.0,
        'args':(50,50)
    }
}


app.autodiscover_tasks(settings.INSTALLED_APPS)

# app.conf.beat_scheduler='django_celery_beat.schedulers.DatabaseScheduler'

@app.task(bind=True)
def debug_task(self):
    print(f'request:{self.request!r}')


