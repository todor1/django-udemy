from email import message
from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
import os
import json
import requests


def home(request):
    if request.method == "POST":
        ticker = request.POST["ticker"].upper()
        api_key = os.getenv("POLYGON_API_KEY")
        # more granular data
        # url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey={api_key}"

        # less granular: daily data
        url = f"https://api.polygon.io/v1/open-close/{ticker}/2024-05-01?adjusted=true&apiKey={api_key}"

        api_request = requests.get(url)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, "home.html", {"api": api})
    else:
        return render(request, "home.html", {"ticker": "Enter a ticker symbol"})


def about(request):
    return render(request, "about.html", {})


def add_stock(request):
    api_key = os.getenv("POLYGON_API_KEY")
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added")
            return redirect("add_stock")
        ticker = request.POST["ticker"].upper()
    else:
        ticker = Stock.objects.all()
        output = []
        for item in ticker:
            # less granular: daily data
            url = f"https://api.polygon.io/v1/open-close/{item.ticker.upper()}/2024-05-01?adjusted=true&apiKey={api_key}"
            api_request = requests.get(url)
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render(request, "add_stock.html", {"ticker": ticker, "output": output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, "Stock has been deleted")
    return redirect("add_stock")
