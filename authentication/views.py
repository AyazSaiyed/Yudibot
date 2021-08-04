# -*- encoding: utf-8 -*-
"""
Developer - Ayaz Saiyed M.
Deployed Code - June 4th, 2021
"""

from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import get_user_model
DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)

User = get_user_model()
status = ''
@csrf_exempt
def login_view(request):
    form = LoginForm(request.POST or None)
    username = ""
    msg = None

    if request.method == "POST":
        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            print("username",username)
            print("password",password)

            # xx = User.objects.all()
            # print(" request " ,request)
            user = authenticate(usersname=username, passwords=password)
            print("user ->",user)
            try:
                a = User.objects.filter(usersname=username,passwords=password)
                for i in a:
                    request.session['uid'] = username
                    print("request.session['uid']",request.session['uid'])
                    print(i.isSales)
                    print(i.isAdmin)
                    print(i.isHR)
                    if i.isSales == True:
                        status = "isSales"
                    if i.isHR == True:
                        status = "isHR"
                        # return redirect("/jobapplicants.html",{'session1':username,'status':status})
                    if i.isAdmin == True:
                        status = "isAdmin"
                    print("status ",status)
                    request.session['status'] = status
                    print(request.session['status'])
                    # return HttpResponse(" logged in ")
                    # return redirect('/')
                    return redirect("/")
                    # return redirect("./tables.html",{'session1':username,'status':status})

            except Exception as e:
                print("exception",e)



            if user is not None:
                # print("found user ",user)
                # request.session["uid"]= username
                # print("username",request.session["uid"])
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


@csrf_exempt
def register_user(request):
    form = SignUpForm(request.POST or None)
    msg     = None
    success = False
    print("register1")
    if request.method == "POST":
        print("register12")

        if not form.is_valid() or form.is_valid:
            print("91")
            AdminPassword = request.POST['admin_password']
            if AdminPassword == "admin786*":
                pass
            else:
                msg = 'Invalid admin secret code'
                success = False 
                return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
            print("AdminPassword",AdminPassword)
            AdminUsers = User.objects.filter(is_superuser=True)
            print("AdminUsers",AdminUsers)
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            password = request.POST['password1']
            email = request.POST['email']
            usertype = request.POST['userType']
            print("firstname",request.POST['first_name'])
            print("lastname",lastname)
            print("password",password)
            print("email",email)
            print("usertype",usertype)
            us = User.objects.create_user(usersname=firstname,username =firstname,first_name=firstname, last_name = lastname, password=password,passwords=password, email=email,is_staff=True)
            cd = form.cleaned_data
            if usertype == "isHR":
                us.isHR = True
            if usertype == "isAdmin":
                us.isAdmin = True
            if usertype == "isSales":
                us.isSales = True
            us.save()
            print("tried")
            print("passed")
            # print(f"u {username}, admin {admin}")
            user = authenticate(username=firstname, password=password)
            msg     = 'Successfully registered.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })


# def logout(request):
#     login_view()
#     return render(request, "accounts/login.html")