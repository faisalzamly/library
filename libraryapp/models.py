from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth.models import User
# Create your models here.
# class admin_login_models(models.Model):

#add
class student_registration_models(models.Model):
    user=models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Roll_Number=models.IntegerField()
    Branch = models.CharField(max_length=50)
    Class  = models.CharField(max_length=50)
    # Student_Image= models.ImageField(upload_to="", blank=True)
    Mobile =models.IntegerField()
    Email=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
