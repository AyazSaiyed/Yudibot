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


admin.site.site_header = "Yudiz Solutions Pvt. Ltd.";
admin.site.site_title = " AI Base Chatbot - Ayaz Saiyed M."
admin.site.index_title = "CHATBOT DASHBOARD"



class Filters(admin.ModelAdmin):
    search_fields = ['enquriy']
    list_per_page = 10
    list_display = ['date','username','enquriy','email','phone']
    list_filter = (
        'date','enquriy'
    )


class JobFilters(admin.ModelAdmin):
    search_fields = ['enquriy']
    list_per_page = 10
    list_display = ['date','candidatename','appliedfor','experience']
    list_filter = (
        'date','appliedfor'
    )

admin.site.register(ClientEnquiries,Filters)
admin.site.register(JobApplicants,JobFilters)
