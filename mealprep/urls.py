from django.urls import path
from .views import (
  ThankView, MealPlanView, MealOptionsDeleteView,
  MealOptionsView, MealOptionsCreateView,
  MealOptionsUpdateView , IngredientCreateView,
  GroceryListView, GroceryListCreateView,
  GroceryListDeleteView,
)

app_name = 'mealprep'

urlpatterns = [
  path('', MealOptionsView.as_view(), name='meal-item-list'),
  path('meal-item-create/', MealOptionsCreateView.as_view(), name='meal-item-create'),
  path('meal-item-update/<int:pk>/', MealOptionsUpdateView.as_view(), name='meal-item-update'),
  path('meal-item-delete/<int:pk>/', MealOptionsDeleteView.as_view(), name='meal-item-delete'),
  path('meal-plan/', MealPlanView.as_view(), name='meal-plan'),
  path('create-item/', IngredientCreateView.as_view(), name='create-ingredient-item'),
  path('grocery-list/', GroceryListView.as_view(), name='grocery-list'),
  path('grocery-list-create/', GroceryListCreateView.as_view(), name='grocery-list-create'),
  path('grocery-list-delete/<int:pk>', GroceryListDeleteView.as_view(), name='grocery-list-delete'),
  path('thanks/', ThankView.as_view(), name='thanks'),
]