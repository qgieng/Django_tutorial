from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'login/index.html')
    
