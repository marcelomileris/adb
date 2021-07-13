"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from person import views

urlpatterns = [
    path('person/', views.person),
    path('person/<int:pk>/', views.person),

    path('person_type/', views.person_type),
    path('person_type/<int:pk>/', views.person_type),

    path('person_media_type/', views.person_media_type),
    path('person_media_type/<int:pk>/', views.person_media_type),

    path('person_media/', views.person_media),
    path('person_media/<int:pk>/', views.person_media),

    path('image/', views.image),

]
