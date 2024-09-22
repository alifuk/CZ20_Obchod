from django.forms import ModelForm, Form, CharField
from viewer.models import Car, Offer
from django.core.exceptions import ValidationError

class CarsForm(ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

def title_validator(text):
  if len(text) < 4:
    raise ValidationError("moc krátké")
  pass

class CleanForm(Form):
  title = CharField(max_length=128, validators=[title_validator])
  desc = CharField(max_length=128, validators=[title_validator])

  def clean_title(self):
    # Každá titulek bude začínat velkým písmenem
    return self.cleaned_data['title'].capitalize()


  pass


