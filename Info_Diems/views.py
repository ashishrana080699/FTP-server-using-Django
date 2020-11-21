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

    return render(request,"home.html")


def search(request):
    return render(request,"search.html")

def find(request):
    return render(request,"search.html",{'path':path})
