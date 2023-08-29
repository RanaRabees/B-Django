

from datetime import date
import datetime
import email
from unicodedata import name
from urllib import request
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from . import views
from earth.models import info
# Create your views here.





def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def partner(request):
    return render(request, 'partner.html')


def participent(request):
    return render(request, 'participent.html')


def packages(request):
    return render(request, 'packages.html')


def tasks(request):
    return render(request, 'tasks.html')


def adventurer(request):
    return render(request, 'adventurer.html')
# def base(request):
#     return render(request,'base.html')


def desired_area(request):
    return render(request, 'desired_area.html')


def discounts(request):
    return render(request, 'discounts.html')


def expertises(request):
    return render(request, 'expertises.html')


def invester(request):
    return render(request, 'invester.html')


def prize_winner(request):
    return render(request, 'prize_winner.html')


def procedures(request):
    return render(request, 'procedures.html')


def techniques(request):
    return render(request, 'techniques.html')


def training_learning(request):
    return render(request, 'training_learning.html')


def subcontact(request):
    b=''
    if  request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=info(name=name,email=email,password=password)
        data.save()        
        b='your message has been sent'     
    return render(request,'index.html',{'b':b})


# def post(request):


# if  request.method == "post":
#     name = request.post.get('name')
#     email = request.post.get('email')
#     phone = request.post.get('phone')
#     desc = request.post.get('desc')
#     contact=contact(name=name,email=email,phone=phone,desc=desc, date = (datetime.today))
#     contact.save()
#     messages.success(request, 'your message has been sent')
#     return render(request, 'contact.html')
