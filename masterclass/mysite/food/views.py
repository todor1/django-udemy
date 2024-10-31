from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView


def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    # template = loader.get_template("food/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "food/index.html", context)


class IndexClassView(ListView):
    # class based view for the index page, replaces the index function
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"

    # def get_queryset(self):
    #     return Item.objects.all()


def item(request):
    return HttpResponse("<h3>This is the item view</h3>")


def detail(request, item_id):
    # return HttpResponse("<h2>Details for item id: " + str(item_id) + "</h2>")
    item = Item.objects.get(pk=item_id)
    context = {"item": item}
    return render(request, "food/detail.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-form.html", context={"form": form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    # pass also the item to the form context, this data is displayed in the form and will be updated/edited
    return render(request, "food/item-form.html", context={"form": form, "item": item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/item-delete.html", context={"item": item})
