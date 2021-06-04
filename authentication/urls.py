# -*- encoding: utf-8 -*-
"""
Developer - Ayaz Saiyed M.
Deployed Code - June 4th, 2021
"""

from django.urls import path
from .views import login_view, register_user
from app import views
urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
	path('logout/',views.logout,name="logout")


]
