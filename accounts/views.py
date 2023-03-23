from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import Signupforms

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = Signupforms(request.POST)
    else:
        form = Signupforms()
    return render(request, "registration/signup", {"form": form})


# def register(request):
#     if request.method == "GET":
#         return render(request, "users/register.html",{"form": Signupforms})
#     elif request.method == "POST":
#         form = Signupforms(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("signup"))
