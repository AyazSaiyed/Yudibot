# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),
	path('bot/', views.index_function, name='index_function'),
	path('', views.index, name='index'),
	path("jobapplicant/", views.jobapplicants, name="jobapplicants"),
    # The home page
  

]
