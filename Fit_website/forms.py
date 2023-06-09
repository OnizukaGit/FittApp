from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import formset_factory

from Fit_website.models import Ingredient, MealTime, Meal, IngredientQuantity
from django.forms.models import inlineformset_factory


User = get_user_model()


class RegisterForm(forms.ModelForm):

    pass1 = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    pass2 = forms.CharField(widget=forms.PasswordInput, label="Powtórz hasło")

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'pass1',
                  'pass2',
                  )
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Email',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ten email jest już w naszej bazie")
        return email


class IngredientsForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        exclude = ('user',)


class MealTimeForm(forms.ModelForm):

    class Meta:
        model = MealTime
        exclude = ('user',)


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        fields = ['ingredient', 'quantity']


class IngredientQuantityForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        fields = ('ingredient', 'quantity')


IngredientQuantityFormSet = inlineformset_factory(Meal, IngredientQuantity, form=IngredientQuantityForm, extra=1)


class MealIngredientForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('name', 'description')


