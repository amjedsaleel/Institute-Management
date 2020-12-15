# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request, name):
        print(name)
        return render(request, 'student/dashboard.html')

    def post(self, request):
        pass


def ppp(request, name):
    return render(request, 'student/dashboard.html')
