# from django.contrib.auth.forms import UserCreationForm
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)
from django import forms
from .models import student_registration_models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


#add
class student_registration_forms(forms.ModelForm):
    Username = forms.CharField(max_length=20)
    First_Name = forms.CharField(max_length=20)
    Last_Name = forms.CharField(max_length=20)
    Email = forms.EmailField()
    Phone_Number = forms.IntegerField()
    Branch = forms.CharField(max_length=20)
    classroom = forms.CharField(max_length=20)
    roll_no = forms.IntegerField()
    # image = forms.ImageField(upload_to="", blank=True)
    Password = forms.CharField(max_length=50)

    class Meta:
        model = student_registration_models
        exclude = ("user",)