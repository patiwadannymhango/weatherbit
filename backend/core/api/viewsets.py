# api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
import requests
from django.conf import settings
from django.http import JsonResponse
from core.auth.permissions import UserPermission

WEATHERBIT_API_KEY = '5bf738c0c48a46eab4cd7bd86aa6bd66'  # Replace with your Weatherbit API key

class WeatherViewSet(viewsets.ViewSet):
    permission_classes = (UserPermission,)
    
    def get_current_weather(self, request):
        city = request.GET.get('city')
        country = request.GET.get('country')
        if city and country:
            url = f"https://api.weatherbit.io/v2.0/current?city={city}&country={country}&key={WEATHERBIT_API_KEY}"
            response = requests.get(url)
            return Response(response.json())
        return Response({"error": "City and country are required"}, status=400)

    def get_forecast_weather(self, request):
        city = request.GET.get('city')
        country = request.GET.get('country')
        if city and country:
            url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city}&country={country}&key={WEATHERBIT_API_KEY}"
            response = requests.get(url)
            return Response(response.json())
        return Response({"error": "City and country are required"}, status=400)
