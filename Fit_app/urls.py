"""
URL configuration for Fit_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Fit_website.views import LoadingPage, Register, Login, Logout, AddIngredients, AddMeal, Summary, SearchIngredientView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoadingPage.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('add-ingredients/', AddIngredients.as_view(), name='add_ingredients'),
    path('add-meal/', AddMeal.as_view(), name='add_meal'),
    path('summary/', Summary.as_view(), name='summary'),
    path('ajax/ingredients/', SearchIngredientView.as_view(), name='ajax_ingredients'),

]
