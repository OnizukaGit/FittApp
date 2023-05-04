from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Fit_website.forms import RegisterForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from Fit_website.models import TimeofDay, MealTime
from django.shortcuts import redirect


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


class Login(LoginView):
    template_name = 'Fit_website/login.html'
    next_page = reverse_lazy('index')
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class Logout(LogoutView):
    template_name = 'Fit_website/index.html'
    next_page = reverse_lazy('login')
