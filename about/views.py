from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .forms import ContactForm


def index(request):
    messages.success(request, 'success')
    return render(request, 'about/index.html')


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about:index')

    return render(request, 'about/contact.html', {'form': form})
