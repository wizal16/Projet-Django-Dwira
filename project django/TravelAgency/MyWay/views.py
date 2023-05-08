from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def destinations(request):
    return render(request,'destinations.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

