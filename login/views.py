from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'login/index.html')
def login(request):
    u = request.POST['username']
    p = request.POST['password']
    stuff = {'username':u,
        'password':p
    }
    return render(request, 'login/main.html', stuff)