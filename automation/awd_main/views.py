from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task


# Create your views here.
def home(request):
    return render(request, "home.html")


def celery_test(request):
    # execute a time-consuming task in the background
    celery_test_task.delay()
    return HttpResponse("<h3> Function executed successfully. Celery is working! </h3>")
