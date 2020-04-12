from django.urls import path
from . import views

app_name='login'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.login, name='login'),
    path('user/in/search/', views.load_main, name='main'),
    
]