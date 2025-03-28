"""
URL configuration for diya_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Welcome to Diyas backend")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include(('api.v1.users_api.urls'),namespace='users_api')) , 
    path('api/v1/content/', include(('api.v1.content_api.urls'),namespace='content_api')) , 
    path('api/v1/vehicle/', include(('api.v1.vehicle_api.urls'),namespace='vehicle_api')) , 
    path('',home,name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
