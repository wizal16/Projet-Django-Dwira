from django import views
from django.urls import path
from .views import *

urlpatterns = [ 
    path('',home, name="home"),
    path('/',destinations, name="destinations"),
    path('/signin',signin, name="signin"),
    path('/signup',signup, name="signup"),

   
]

