from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=C70116DD-59B9-4E6D-8D57-0383C8DA05C3")    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})