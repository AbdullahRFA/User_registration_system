from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User

# Create your views here.
def HomePage(request):
    return render(request,'home.html')
def Login(request):
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
