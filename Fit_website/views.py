from django.shortcuts import render
from django.views import View


class LoadingPage(View):
    def get(self, request):
        return render(request, 'Fit_website/index.html')
