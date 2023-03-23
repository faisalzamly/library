from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm

# from .models import student_registration_models
# from .forms import sinup
# from .forms import sinup
from .models import *

# from libraryapp.forms import CustomUserCreationForm,UserCreationForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def add_book(request):
    return render(request, "add_book.html")


def admin_login(request):
    return render(request, "admin_login.html")


def student_registration(request):
    if request.method == "GET":
        return render(request, "student_registration.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
    return render(request, "student_registration.html", {"form": form})
####index

def student_login(request):
    return render(request, "student_login.html")
