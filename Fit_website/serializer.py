from Fit_website.models import Ingredient, IngredientQuantity, MealTime, TimeofDay, Meal
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ('user',)


class IngredientQuantitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IngredientQuantity
        fields = '__all__'


class MealTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealTime
        exclude = ('user',)


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        exclude = ('user',)


class TimeofDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeofDay
        fields = '__all__'


