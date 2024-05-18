from django.shortcuts import render, redirect
from .forms import PasswordForm
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def galerie(request):
    passwort_objekt = PassWord.objects.first()
    GALLERY_PASSWORD = passwort_objekt.text

    images = GalerieImage.objects.all().order_by('-id')
    ctx = {"images": images}

    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == GALLERY_PASSWORD:
                return render(request, 'home/galerie.html', ctx)
            else:
                form.add_error('password', 'Falsches Passwort')
    else:
        form = PasswordForm()
    
    return render(request, 'home/password_protected.html', {'form': form})

def review(request):
    enterys = ReviewEntery.objects.all().order_by('-id')
    ctx = {"enterys": enterys} 
    return render(request, "home/review.html", ctx)
