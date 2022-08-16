from django.db import models

# Create your models here.
class MealItem(models.Model):
  meal = models.CharField(max_length=50, unique=True)
  ingredients = models.ManyToManyField('Ingredient')
  recipe = models.TextField(blank=True, null=True)
  
  class Meta:
    verbose_name = 'Meal'
  
  def __str__(self):
    return self.meal
  
  
class Ingredient(models.Model):
  ingredient_item = models.CharField(max_length=100, unique=True)
    
  def __str__(self):
    return self.ingredient_item
  

class GroceryList(models.Model):
  grocery_item = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
      return self.grocery_item
  

class MealPlan(models.Model):
  id = models.CharField(max_length=50, primary_key=True)
  meal_item = models.ForeignKey(MealItem, on_delete=models.CASCADE)
  
  class Meta:
    verbose_name_plural = 'Meal Plan'
  
  def __str__(self):
      return self.id
