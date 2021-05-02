from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [

    path('', include('login.urls', namespace="login")),
    path('admin/', admin.site.urls),
    path('aplicacions/', include('aplicacions.urls', namespace="aplicacions")),
    path('batxilleratProjecte/', include('batx_seminaris.urls', namespace="batxSeminaris")),
    # Path obligatori allauth
    path('accounts/', include('allauth.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]