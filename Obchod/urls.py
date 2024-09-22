"""Obchod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from viewer.views import MainPageView, CarsView, OffersView, CarsUpdateView, CarsDeleteView
from viewer.views import CarsCreateView, CarsUpdateView, CarsDeleteView
from viewer.models import Car, Offer, CarFeature

from django.contrib.auth.views import LogoutView

admin.site.register(Car)
admin.site.register(Offer)
admin.site.register(CarFeature)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('offers/', OffersView.as_view(), name='offers'),
    path('cars/create/', CarsCreateView.as_view(), name='create_car'),
    path('cars/update/<pk>', CarsUpdateView.as_view(), name='update_car'),
    path('cars/delete/<pk>', CarsDeleteView.as_view(), name='delete_car'),


    path('users/logout', LogoutView.as_view(), name='logout'),

]
