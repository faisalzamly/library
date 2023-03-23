from .views import index, add_book, admin_login, student_registration, student_login
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
    path("add_book/", add_book, name="add_book"),
    path("admin_login/", admin_login, name="admin_login"),
    path("student_registration/", student_registration, name="student_registration"),
    path("student_login/", student_login, name="student_login"),
]
