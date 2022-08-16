from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MealItem)
admin.site.register(models.Ingredient)
admin.site.register(models.GroceryList)
admin.site.register(models.MealPlan)