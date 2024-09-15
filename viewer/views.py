from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from viewer.models import Car, Offer

class MainPageView(TemplateView):
  template_name = 'index.html'
  extra_context = {
    'all_cars': Car.objects.all(),
    'all_offers': Offer.objects.all()
  }