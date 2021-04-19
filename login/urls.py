from django.urls import path, include
from .views import GoogleLoginView, GoogleLogoutView
app_name = "login"
urlpatterns = [
    path("", GoogleLoginView.as_view(), name="account_login"),
    path("logout/", GoogleLogoutView.as_view(), name="logout"),
]
