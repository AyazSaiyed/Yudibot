from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Course,Reg
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
	if request.method=="POST":
		r = Reg.objects.filter(uname=request.POST["txtuser"],pwd=request.POST["txtpass"])
		if r.count()>0:
		  request.session["uid"]=request.POST["txtuser"]	
		  return redirect('/dbapp/index')
		else:
		  return HttpResponse("Invalid Userid and password")  
	return render(request,"dbapp/login.html")	

def reg(request):
	if request.method=="POST":
		r = Reg(uname=request.POST["txtuser"],pwd=request.POST["txtpass"],email=request.POST["txtemail"],mobile=request.POST["txtmobile"])
		r.save()
		return redirect('login')
	return render(request,"dbapp/reg.html")	

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
	
	if request.session.has_key('uid'):
		uid = request.session["uid"]
		if request.method=="POST":
			obj = Course(courseid=request.POST["txtrno"],coursename=request.POST["txtsname"],coursefees=request.POST["txtbranch"])
			obj.save()
			return render(request,"dbapp/index.html",{"res":"data inserted successfully"})
		return render(request,"dbapp/index.html",{'key':uid})
	else:
		return redirect('login')	 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
	del request.session["uid"]
	return redirect('login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)	
def course(request):
	if request.session.has_key('uid'):
		res = Course.objects.all()
		return render(request,"dbapp/course.html",{'data':res})
	else:
		return redirect('login')		

def editrec(request):
	if request.method=="POST":
		e=request.POST["tcid"]
		m=request.POST["tcname"]
		f=request.POST["tfee"]
		s = Course.objects.get(pk=request.POST["txtid"])
		s.courseid=e
		s.coursename=m
		s.coursefees=f
		s.save()
		return redirect('course')
	else:
		res = Course.objects.get(pk=request.GET["q"])
		return render(request,"dbapp/editrec.html",{'data':res})
   

def deleterec(request):
	if request.method=="POST":
	 res = Course.objects.get(pk=request.POST["txtid"])
	 res.delete()
	 return redirect('course')
	else:
	  res = Course.objects.get(pk=request.GET["q"])
	  return render(request,"dbapp/deleterec.html",{'data':res}) 