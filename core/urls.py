# -*- encoding: utf-8 -*-
"""
Developer - Ayaz Saiyed M.
Deployed Code - June 4th, 2021
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url
from app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    url("", include("app.urls")),
    # url("", include("app.urls")),

    # path('^/bot',views.index_function,name="index_function")
]
