from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Information
import os
# Create your views here.

def home(request):
    return render(request,"home.html")

def info(request):
    return render(request,"info.html")

def info_upload(request):
    department=request.POST["department"]
    category=request.POST["category"]
    startdate=request.POST["startdate"]
    enddate=request.POST["enddate"]
    duration=request.POST["duration"]
    participants=request.POST["participants"]
    year=request.POST["year"]
    semister=request.POST["semister"]
    facultyname=request.POST["facultyname"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    message=request.POST["message"]
    if request.method=='POST':
        myfile=request.FILES["file"]
        fs=FileSystemStorage()
        fs.save(myfile.name, myfile)

    obj=Information(department=department,category=category,startdate=startdate,enddate=enddate,duration=duration,participants=participants,year=year,semister=semister,facultyname=facultyname,email=email,phone=phone,myfile=myfile.name,message=message)
    obj.save()

    return render(request,"home.html")


def search(request):
    return render(request,"search.html")

def find(request):
    departmant=request.POST["department"]
    year=request.POST["year"]
    semister=request.POST["semister"]
    category=request.POST["category"]
    data=Information.objects.filter(department__iexact=departmant).filter(year__iexact=year).filter(semister__iexact=semister).filter( category__iexact=category)
    
    path=[] 
    name=[]
    if len(data)!=0:
        for value in data:
            path.append('/media/'+value.myfile)
        for obj in data:
            name.append(obj.myfile)
    print(path)
    return render(request,"search.html",{'path':path})
