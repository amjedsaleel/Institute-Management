from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .forms import ContactForm


def index(request):
    return render(request, 'about/index.html')


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contacting with us. We will connect with you')
            return redirect('about:index')

    return render(request, 'about/contact.html', {'form': form})
