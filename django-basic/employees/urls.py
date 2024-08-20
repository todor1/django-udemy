from django.urls import path
from . import views

urlpatterns = [
    # the employees part of the URL is already handled in the mysite/urls.py file, at project level
    # the path function is used to create a URL pattern, using the id of the employee as a parameter on app level
    path('<int:pk>/', views.employee_detail, name="employee_detail"),
]
