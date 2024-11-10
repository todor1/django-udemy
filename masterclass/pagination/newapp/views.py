from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator  # , PageNotAnInteger, EmptyPage


# Create your views here.
def movie_list(request):
    movie_objects = Movie.objects.all()
    movie_name = request.GET.get("movie_name")
    if movie_name != "" and movie_name is not None:
        # movie_objects = movie_objects.filter(name=movie_name) # exact match
        movie_objects = movie_objects.filter(
            name__icontains=movie_name
        )  # case-insensitive match

    paginator = Paginator(movie_objects, per_page=3)
    page = request.GET.get("page")
    # if another variable name is used, it should be passed also as context to the template
    movie_objects = paginator.get_page(page)
    return render(request, "newapp/movie_list.html", {"movie_objects": movie_objects})
