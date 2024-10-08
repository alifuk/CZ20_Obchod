from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import (UserCreationForm)

from django.views.generic import TemplateView, CreateView, DeleteView, FormView
from django.views.generic import UpdateView

from viewer.models import Car, Offer, Comment
from django.urls import reverse_lazy
from viewer.forms import CarsForm, CleanForm, CommentForm

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

class SignUpView(CreateView):
  template_name = 'form.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('login')

class UserView(TemplateView):
  template_name = "user.html"




class ExampleForm(FormView):
    template_name = 'form.html'
    form_class = CleanForm
    success_url = reverse_lazy('cars')

    def form_valid(self, form):
      result = super().form_valid(form)

      return result


class CarsDetailedView(TemplateView):
  template_name = 'car_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data( **kwargs)
    context["car_detail"] = Car.objects.get(pk=int(kwargs["pk"]))
    context["car_comments"] = Comment.objects.filter(car__pk=int(kwargs["pk"]))
    return context

class CommentCreateView(FormView):
  template_name = 'form.html'
  form_class = CommentForm
  success_url = reverse_lazy("cars")

  def form_valid(self, form):
    new_comment : Comment = form.save(commit=False)
    new_comment.car = Car.objects.get(pk=int(self.kwargs["car_pk"]))
    new_comment.save()
    return super().form_valid(form)

#CRONTAB SOUBOR OBSAH: * * * * 3 python3 send_email_to_users.py >/dev/null 2>&1
#Generování obsahu pro CRON soubor je https://crontab-generator.org/
def send_emails_to_user(request):
  #ZDE přijde kód pro odeslání emailů...
  print(f"Máme nová auta {Car.objects.all()} ")

  return HttpResponse("vše OK")


def api_get_all_cars(request):
  all_cars = Car.objects.all()
  json_all_cars = {}
  for car in all_cars:
    json_all_cars[car.pk] = {
      "brand": str(car.brand),
      "color": str(car.color)
    }

  return JsonResponse(json_all_cars)

def api_get_all_comments(request):
  json_all_comments = { comment.pk: {"text":str(comment.text)} for comment in Comment.objects.all()}
  return JsonResponse(json_all_comments)

