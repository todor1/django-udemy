import os
from celery import Celery

# set the default django settings module for the 'celery' program
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "awd_main.settings")

# sets up the new celery app for our django project (awd_main)
app = Celery("awd_main")

# namespace='CELERY' means that all celery-related configuration keys will have a CELERY_ prefix
# in the Django settings file
app.config_from_object("django.conf:settings", namespace="CELERY")

# load task modules from all registered Django app configs
app.autodiscover_tasks()


# the decorator below is used to create a task that can be used in the celery worker and executed asynchronously in the background
@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
