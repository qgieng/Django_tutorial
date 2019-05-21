from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.urls import reverse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login/index.html')
def login(request):
    u = request.POST['username']
    p = request.POST['password']
    try:
        check = User.objects.get(user_name = u)
    except:
        return render(request, 'login/index.html', {"message": "User does not exist"})


    if(check.check_password(p)):
        stuff = {'message':"success",'password':p}
        return render(request, 'login/main.html', stuff)
    else:
        stuff = {"message":"wrong information"}
        return render(request, 'login/index.html', stuff)
