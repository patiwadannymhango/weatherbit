import requests
from django.http import JsonResponse
from django.conf import settings

WEATHERBIT_API_KEY = 'your_api_key_here'  # Add your API key

def get_current_weather(request):
    city = request.GET.get('city')
    country = request.GET.get('country')
    if city and country:
        url = f"https://api.weatherbit.io/v2.0/current?city={city}&country={country}&key={WEATHERBIT_API_KEY}"
        response = requests.get(url)
        return JsonResponse(response.json())
    return JsonResponse({"error": "City and country are required"}, status=400)

def get_forecast_weather(request):
    city = request.GET.get('city')
    country = request.GET.get('country')
    if city and country:
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city}&country={country}&key={WEATHERBIT_API_KEY}"
        response = requests.get(url)
        return JsonResponse(response.json())
    return JsonResponse({"error": "City and country are required"}, status=400)
