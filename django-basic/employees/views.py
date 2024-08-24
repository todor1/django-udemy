
from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.http import HttpResponse

# Create your views here.
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    # return HttpResponse(employee)
    return render(request, "employee_detail.html", {"employee": employee})