from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('login.urls', namespace="login")),
    path('admin/', admin.site.urls),
    # Path obligatori allauth
    path('accounts/', include('allauth.urls')),
]
