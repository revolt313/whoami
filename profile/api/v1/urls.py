from django.urls import path
from rest_framework.routers import DefaultRouter
from profile.api.v1 import views

# Create your urls here.


# Create a router and register our viewsets with it.
app_name = "profile"

router = DefaultRouter()
router.register('register', views.RegisterNewUser)
router.register('users', views.UserViewSet)
router.register('profiles', views.ProfileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('token-auth/', views.obtain_auth_token),
] + router.urls