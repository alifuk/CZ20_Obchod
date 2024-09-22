from django.forms import ModelForm
from viewer.models import Car, Offer

class CarsForm(ModelForm):
  class Meta:
    model = Car
    fields = '__all__'



