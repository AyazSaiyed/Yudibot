# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth import get_user_model
User = get_user_model()
UserTypeChoices = [
    ('isHR', 'HR'),
    ('isSales', 'Sales'),
    ('isAdmin', 'Admin'),
]

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "value"       : "",
                "class"       : "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "value"       : "",                
                "class"       : "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    admin_password = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Admin Secret Code ',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Secret Code'}))
    first_name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=20, min_length=4, required=True, help_text='Required: Last Name',
                               widget=(forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'})))
    email = forms.EmailField(required=True,max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'})))
    password1 = forms.CharField(required=True,label=('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Password'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(required=True,label=('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm Password'}),
                                help_text=('Just Enter the same password, for confirmation'))
    userType = forms.ChoiceField(required=True, help_text='Required: User Type ( HR, Sales or Admin ) ', widget=forms.RadioSelect, choices=UserTypeChoices)
    class Meta:
        model = User
        fields = ('userType', 'first_name', 'last_name', 'email', 'password1', 'password2','admin_password')