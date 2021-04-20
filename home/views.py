from django.shortcuts import render,HttpResponse
from . import models

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'projects.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        zip=request.POST['zip']
        ins = models.contact(name=name,email=email,address=address,city=city,zip=zip)
        ins.save()
        print("dfd")

    return render(request,'contact.html')