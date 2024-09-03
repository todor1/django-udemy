from django.shortcuts import render


def home(request):
    import os
    import json
    import requests

    ticker = "AAPL"
    api_key = os.getenv("POLYGON_API_KEY")
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey={api_key}"

    api_request = requests.get(url)
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, "home.html", {"api": api})


def about(request):
    return render(request, "about.html", {})
