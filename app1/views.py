from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def HomePage(request):
    return render(request,'home.html')
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=username,password=password)
        if user is None:
            return HttpResponse("Username or password is incorrect")
        
        login(request,user)
        return redirect('homepage')
        
        
    return render(request,'login.html')

def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            return HttpResponse("Your password and confirm password does not match")
        else:
            my_user = User.objects.create_user(username,email,password1)
            my_user.save()
        if my_user:
            return redirect('login')
        
        print(username,email,password1,password2)
    return render(request,'signup.html')

def Logout(request):
    logout(request)
    return redirect('login')