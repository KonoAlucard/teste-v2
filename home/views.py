from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import os
from django.conf import settings


def home(request):
    if request.method == "GET":
       return render (request, "home.html")
    elif request.method == "POST":
       file = request.FILES["my_file"]
       file_name = file.__getattribute__('name')

       img = Image.open(file)
       path = os.path.join(f'{settings.BASE_DIR}\\home\\media', file_name)
       img = img.save(path)


       print(file)

       return render (request, "home.html")
    
    
    

    


def login (request):
    if request.method == "GET":
       return render (request, "login.html")
    elif request.method == "POST":
       return render (request, "home.html")


def galeria (request):
    if request.method == "GET":
       path = "/home/media"
       files = os.listdir(f'{settings.BASE_DIR}\\home\\media')
       images = [{"name":image, "url":f'{path}/{image}'}for image in files]
       print(images)
       return render(request, "galeria.html", {"images": images})
    
    
 