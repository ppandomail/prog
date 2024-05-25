"""
URL configuration for django_01_apis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from django_01_apis.index import hola, chau, fecha, edad

urlpatterns = [
    path('admin/', admin.site.urls),    # tupla que viene por default
    path('hola/', hola),
    path('chau/', chau),
    path('fecha/', fecha),
    path('edad/<int:edad>/<int:año>', edad),
]
