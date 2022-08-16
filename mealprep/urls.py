from django.urls import path
from .views import (
  ThankView, MealPlanView, 
  MealOptionsView, MealOptionsCreateView,
  MealOptionsUpdateView , IngredientCreateView,
  GroceryListView, GroceryListCreateView,
)

app_name = 'mealprep'

urlpatterns = [
  path('', MealOptionsView.as_view(), name='meal-item-list'),
  path('meal-item-create/', MealOptionsCreateView.as_view(), name='meal-item-create'),
  path('meal-item-update/<int:pk>/', MealOptionsUpdateView.as_view(), name='meal-item-update'),
  path('meal-plan/', MealPlanView.as_view(), name='meal-plan'),
  path('create-item/', IngredientCreateView.as_view(), name='create-ingredient-item'),
  path('grocery-list/', GroceryListView.as_view(), name='grocery-list'),
  path('grocery-list-create/', GroceryListCreateView.as_view(), name='grocery-list-create'),
  path('thanks/', ThankView.as_view(), name='thanks'),
]
