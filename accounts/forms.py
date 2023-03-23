from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Signupforms(UserCreationForm):
    class Meta:
        module = User
        fields = ["usernam", "email", "pass1", "pass2"]


from .models import Profile


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
