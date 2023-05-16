from rest_framework import routers
from django.urls import include,path
from Fit_website.views import IngredientViewSet, MealViewSet, IngredientQuantityViewSet,\
    MealTimeViewSet, TimeofDayViewSet


routers = routers.DefaultRouter()
routers.register(r'ingredient', IngredientViewSet)
routers.register(r'meal', MealViewSet)
routers.register(r'mealtime', MealTimeViewSet)
routers.register(r'ingredientquantity', IngredientQuantityViewSet)
routers.register(r'timeofday', TimeofDayViewSet)

urlpatterns = [
    path('api/', include(routers.urls)),
]