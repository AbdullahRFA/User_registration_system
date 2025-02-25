from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def HomePage(request):
    return render(request,'home.html')
def Login(request):
    return render(request,'login.html')

def SignUp(request):
    return render(request,'signup.html')
