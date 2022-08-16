from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.views.generic import (
  FormView, TemplateView, ListView, CreateView,
  DeleteView, UpdateView
)

from .models import MealItem, Ingredient, GroceryList, MealPlan
from .forms import MealItemForm

# Create your views here.
class ThankView(TemplateView):
  template_name = 'mealprep/thanks.html'


class FormListView(FormMixin, ListView):
  def get(self, request, *args, **kwargs):
    form_class = self.get_form_class()
    self.form = self.get_form(form_class)
    
    
    self.object_list = self.get_queryset()
    allow_empty = self.get_allow_empty()
    if not allow_empty and len(self.object_list) == 0:
      raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                    % {'class_name': self.__class__.__name__})
      
    context = self.get_context_data(object_list=self.object_list, form=self.form)
    return self.render_to_response(context)
  
  def post(self, request, *args, **kwargs):
    return self.get(request, *args, **kwargs)
  
  
class MealOptionsView(FormListView):
  
  template_name = 'mealprep/meal_options.html'
  model = MealItem
  
  form_class = MealItemForm
  
  def post(self, request, *args, **kwargs):
    meal = MealItem.objects.get(meal=self.request.POST['meal'])
    meal_recipe = meal.recipe
    
    meal_ingredient_objects = meal.ingredients.all()
    grocery_objects = GroceryList.objects.all()
    meal_plan_objects = MealPlan.objects.all()
    
    # Grocery handler
    ingredient_list = []
    for ingred in meal_ingredient_objects:
      stringify = str(ingred)
      ingredient_list.append(stringify)
    
    grocery_list = []
    for grocery in grocery_objects:
      stringify = str(grocery)
      grocery_list.append(stringify)
      
    for ingred in ingredient_list:
      if ingred not in grocery_list:
        add_grocery = GroceryList(grocery_item=ingred)
        add_grocery.save()
        
    # Meal plan handler
    meal_plan_list = []
    for meal_item in meal_plan_objects:
      stringify = str(meal_item)
      meal_plan_list.append(stringify)  
    
    meal_item = meal
    id = str(meal)
    if id not in meal_plan_list:
      meal_plan = MealPlan(id=id, meal_item=meal_item)
      meal_plan.save()
    
    return super().post(request, *args, **kwargs)


class MealOptionsCreateView(CreateView):
  model = MealItem
  fields = '__all__'
  success_url = reverse_lazy('mealprep:meal-item-list')
  
  
class MealOptionsUpdateView(UpdateView):
  model=MealItem
  fields='__all__'
  success_url=reverse_lazy('mealprep:meal-item-list')
  

class IngredientCreateView(CreateView):
  model = Ingredient
  fields = '__all__'
  success_url = reverse_lazy('mealprep:meal-item-create')


class MealPlanView(ListView):
  template_name = 'mealprep/meal_plan.html'
  model = MealPlan
  

class GroceryListView(ListView):
  template_name = 'mealprep/grocery_list.html'
  model = GroceryList
  

class GroceryListCreateView(CreateView):
  model=GroceryList
  fields='__all__'
  success_url=reverse_lazy('mealprep:grocery-list')