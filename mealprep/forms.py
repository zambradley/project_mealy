from django import forms
from .models import MealItem

class MealItemForm(forms.Form):
  meal = forms.HiddenInput()