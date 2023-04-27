from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Fit_website.forms import RegisterForm


class LoadingPage(View):
    def get(self, request):
        return render(request, 'Fit_website/index.html')


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
