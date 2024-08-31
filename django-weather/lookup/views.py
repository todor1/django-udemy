import re
from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests

    category_description = ""
    category_color = ""

    if request.method == "POST":
        zipcode = request.POST["zipcode"]
        api_request = requests.get(
            f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=C70116DD-59B9-4E6D-8D57-0383C8DA05C3"
        )
        # return render(request, "home.html", {"zipcode": zipcode})
    else:
        # default zip code for a get request to the home page
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=C70116DD-59B9-4E6D-8D57-0383C8DA05C3"
        )

    try:
        api = json.loads(api_request.content)

        if api[0]["Category"]["Name"] == "Good":
            category_description = "(0-50) Air quality is considedered satisfactory..."
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_description = "(51-100) Air quality is acceptable; for some pollutants - health concern..."
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "USG":
            category_description = "(101-150) Greater risk from exposure to ozone..."
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_description = "(151+) Спасявай се, Спасиев..."
            category_color = "unhealthy"
    except Exception as e:
        api = "Error..."

    return render(
        request,
        "home.html",
        {
            "api": api,
            "category_description": category_description,
            "category_color": category_color,
        },
    )


def about(request):
    return render(request, "about.html", {})
