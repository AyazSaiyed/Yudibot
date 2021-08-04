# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

'''Developer   - Ayaz Saiyed M.
   Last update - April 8, 2021
   Department  - AI/ML
'''

from django.contrib import admin
from .models import ClientEnquiries,JobApplicants
# Register your models here.

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


admin.site.site_header = "Yudiz Solutions Pvt. Ltd.";
admin.site.site_title = " AI Base Chatbot - Ayaz Saiyed M."
admin.site.index_title = "YUDIBOT DASHBOARD"




class Filters(admin.ModelAdmin):
    # search_fields = ['enquriy']
    list_per_page = 10
    list_display = ['date','username','enquriy','email','phone','onhold','active','inactive']
    list_filter = (
        'date','enquriy','onhold','active','inactive'
    )
    search_fields = ("enquriy__startswith", 'username__startswith')

class JobFilters(admin.ModelAdmin):
    # search_fields = ['enquriy']
    list_per_page = 10
    list_display = ['date','candidatename','appliedfor','experience','resumeurl','selected','pending']
    list_filter = (
        'date','appliedfor','experience','selected','rejected','pending'
    )
    search_fields = ("appliedfor__startswith", )


admin.site.register(ClientEnquiries,Filters)
admin.site.register(JobApplicants,JobFilters)
