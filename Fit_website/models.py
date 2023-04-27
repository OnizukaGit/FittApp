from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    gramme = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calories = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantity')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.quantity)


class TimeofDay(models.Model):
    options = (
        ('Śniadanie','Śniadanie'),
        ('Obiad', 'Obiad'),
        ('Kolacja', 'Kolacja'),
    )

    name = models.CharField(choices=options)

    def __str__(self):
        return self.name


class MealTime(models.Model):
    options = (
        ('Poniedziałek','Poniedziałek'),
        ('Wtorek','Wtorek'),
        ('Środa','Środa'),
        ('Czwartek','Czwartek'),
        ('Piątek','Piątek'),
        ('Sobota','Sobota'),
        ('Niedziela','Niedziela'),
    )

    name = models.CharField(choices=options)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    timeofday = models.ForeignKey(TimeofDay, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name