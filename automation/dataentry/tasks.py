from awd_main.celery import app
import time
from django.core.management import call_command
from django.contrib import messages


# applying the decorator converts the function to a celery task
@app.task
def celery_test_task():
    time.sleep(10)  # siumulation of a time-consuming task (taking 10s to complete)
    print("Celery is working!")
    return "Celery task executed successfully!"


@app.task
def import_data_task(full_path, model_name):
    # trigger the import_data command
    try:
        call_command("importdata", full_path, model_name)
    except Exception as e:
        raise e
    return "Data imported successfully"
