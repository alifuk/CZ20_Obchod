from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, CreateView, DeleteView
from django.views.generic import UpdateView
from viewer.models import Car, Offer
from django.urls import reverse_lazy
from viewer.forms import CarsForm

class MainPageView(TemplateView):
  template_name = 'index.html'
  extra_context = {
    'all_cars': Car.objects.all(),
    'all_offers': Offer.objects.all()
  }

class CarsView(TemplateView):
  template_name = 'cars.html'
  extra_context = {
    'all_cars': Car.objects.all()
  }

class CarsCreateView(LoginRequiredMixin, CreateView):
  template_name = 'form.html'
  form_class = CarsForm
  success_url = reverse_lazy("cars")

class CarsUpdateView(PermissionRequiredMixin, UpdateView):
  template_name = 'form.html'
  model = Car
  form_class = CarsForm
  success_url = reverse_lazy('cars')
  permission_required = 'viewer.add_carfeature'

class CarsDeleteView(DeleteView):
  template_name = 'car_confirm_delete.html'
  model = Car
  success_url = reverse_lazy('cars')

class OffersView(TemplateView):
  template_name = 'offers.html'
  extra_context = {
    'all_offers': Offer.objects.all()
  }


class UserView(TemplateView):
  template_name = "user.html"

