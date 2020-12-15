# Django
from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self, request, name):
        return render(request, 'institute/dashboard.html')

    def post(self, request):
        pass

