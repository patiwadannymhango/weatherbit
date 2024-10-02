from rest_framework_nested import routers
from django.urls import path
from core.api.viewsets import WeatherViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet, LogoutViewSet



router = routers.SimpleRouter()

##### USER ######
router.register(r"user", UserViewSet, basename='user')
##### AUTH ######
router.register(r"auth/register", RegisterViewSet, basename='auth-register')
router.register(r"auth/login", LoginViewSet, basename='auth-login')
router.register(r"auth/refresh", RefreshViewSet, basename='auth-refresh')
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")

#### WEATHERBIT #####
router.register(r'weather', WeatherViewSet, basename='weather')

# Define additional routes for custom actions
weather_list = WeatherViewSet.as_view({
    'get': 'get_current_weather'
})

forecast_list = WeatherViewSet.as_view({
    'get': 'get_forecast_weather'
})

# Custom routes for specific actions
urlpatterns = [
    *router.urls,
    path('current/', weather_list, name='current_weather'),
    path('forecast/', forecast_list, name='forecast_weather'),
]
