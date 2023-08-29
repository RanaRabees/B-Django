
from django.http import HttpResponse
from django.shortcuts import render
from . import views

# Create your views here.


def home(request):
    data = {'v' : "THIS IS MY CITY VIEW"}
    return render(request,'earth/home.html', data )