from rest_framework_nested import routers
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

##### SLIPTA LAB PROFILE ######

# router.register(r"slipta/lab_profile",SliptaLabProfileViewSet, basename="slipta-lab-profile")



urlpatterns = [
    *router.urls,
    # *slipta_lab_profiles_router.urls
]