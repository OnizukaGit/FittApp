from django.contrib import admin
from Fit_website.models import Ingredient, MealTime, Meal, TimeofDay, IngredientQuantity


admin.site.register(Ingredient)
admin.site.register(MealTime)
admin.site.register(Meal)
admin.site.register(TimeofDay)
admin.site.register(IngredientQuantity)