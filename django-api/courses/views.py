from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer


# Create your views here.
def home(request):
    return render(request, "home.html")


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


