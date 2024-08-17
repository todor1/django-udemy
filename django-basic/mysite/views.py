from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

# def home(request):
#     return HttpResponse("<h3>Hello, Django!</h3>")


def home(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request=request, template_name="home.html", context=context)
    # return render(request=request, template_name="home.html")
