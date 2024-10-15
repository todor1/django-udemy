from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader


def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    # template = loader.get_template("food/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "food/index.html", context)


def item(request):
    return HttpResponse("<h3>This is the item view</h3>")
