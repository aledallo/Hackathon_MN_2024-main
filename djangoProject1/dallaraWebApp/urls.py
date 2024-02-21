from django.contrib import admin
from django.urls import path

from dallaraWebApp import views

urlpatterns = [
    path("homepage_director", views.homepage_director, name="director"),
    path("", views.index, name="index"),
    path("homepage_employee", views.homepage_employee, name="employee"),
    path("homepage_human_resources", views.homepage_human_resources, name="human_resources"),
    path("login", views.login_view, name="login_view"),
]
