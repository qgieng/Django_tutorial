from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.urls import reverse
from .models import User

from . import request_yelp
# Create your views here.
def index(request):
    return render(request, 
                'login/index.html')

def login(request):
    try:
        user = request.POST['username']
        password = request.POST['password']
        check = User.objects.get(
                                user_name = user)
    except:
        return render(request, 
                    'login/index.html',
                     {"message": "User does not exist"})

    if(check.check_password(password)):
        dict_k = {'message':"success",
                'password':password}
        return redirect('./in/search/')
    else:
        dict_k = {"message":"Wrong password", 
                'username':user}
        return render(request, 
                    'login/index.html', 
                    dict_k)

        
def load_main(request):
    try:
        query_term= request.GET['query']
        query_location = request.GET['location']

        query_result = request_yelp.query_api(query_term, 
                                         query_location)
        
        dict_json = {'query': query_term, 
                    'term':query_term,
                    'location':query_location,
                    'query_result': list(query_result.values())}

        return render(request, 
                    'login/main.html', 
                    dict_json)
    except Exception as exc:
        #print(exc)
        return render(request, 
                        'login/main.html')



    