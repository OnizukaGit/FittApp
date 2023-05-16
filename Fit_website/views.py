from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Fit_website.forms import RegisterForm, IngredientsForm, MealTimeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from Fit_website.models import Meal, TimeofDay, MealTime, Ingredient, IngredientQuantity
from .forms import MealForm, IngredientQuantityFormSet
from rest_framework import viewsets
from Fit_website.serializer import IngredientSerializer, MealSerializer, MealTimeSerializer,\
    IngredientQuantitySerializer, TimeofDaySerializer


class LoadingPage(View):
    def get(self, request):
        time_of_days = TimeofDay.objects.all()
        meal = None
        if request.user.is_authenticated:
            meal = MealTime.objects.filter(timeofday__name="Śniadanie", user=request.user)
        return render(request, 'Fit_website/index.html',
                      context={'time_of_days': time_of_days,
                               'meal': meal,
                               })


class Register(CreateView):
    template_name = 'Fit_website/register.html'
    success_url = reverse_lazy('index')
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['pass1'])
        self.object.save()
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return self.get(reverse_lazy('register'))


class Login(LoginView):
    template_name = 'Fit_website/login.html'
    next_page = reverse_lazy('index')
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class Logout(LogoutView):
    template_name = 'Fit_website/index.html'
    next_page = reverse_lazy('login')


class AddIngredients(CreateView):
    template_name = 'Fit_website/add_ingredients.html'
    success_url = reverse_lazy('index')
    form_class = IngredientsForm

    def form_valid(self, form):
        isinstance = form.save(commit=False)
        isinstance.user = self.request.user
        isinstance.save()
        return super().form_valid(form)


class Summary(CreateView):
    template_name = 'Fit_website/summary.html'
    success_url = reverse_lazy('index')
    form_class = MealTimeForm

    def form_valid(self, form):
        isinstance = form.save(commit=False)
        isinstance.user = self.request.user
        isinstance.save()
        return super().form_valid(form)


class AddMeal(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'Fit_website/add_meal.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['ingredient_formset'] = IngredientQuantityFormSet(self.request.POST)
        else:
            data['ingredient_formset'] = IngredientQuantityFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']
        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            if ingredient_formset.is_valid():
                ingredient_formset.instance = self.object
                ingredient_formset.save()
                print('Formset is valid')
            else:
                print(ingredient_formset.errors)
        return super().form_valid(form)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealTimeViewSet(viewsets.ModelViewSet):
    queryset = MealTime.objects.all()
    serializer_class = MealTimeSerializer


class IngredientQuantityViewSet(viewsets.ModelViewSet):
    queryset = IngredientQuantity.objects.all()
    serializer_class = IngredientQuantitySerializer


class TimeofDayViewSet(viewsets.ModelViewSet):
    queryset = TimeofDay.objects.all()
    serializer_class = TimeofDaySerializer
