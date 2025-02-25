from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password")  # Add error message
            return redirect('login')  # Redirect back to login page

        login(request, user)
        return redirect('homepage')  # Redirect to the homepage if login is successful
        
    return render(request, 'login.html')


def SignUp(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')  # Redirect back to the signup page
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken! Try another.")
            return redirect('signup')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered! Try logging in.")
            return redirect('signup')

        # Create and save the user
        my_user = User.objects.create_user(username=username, email=email, password=password1)
        my_user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Redirect to login after successful signup

    return render(request, 'signup.html')


def Logout(request):
    logout(request)
    return redirect('login')

def About(request):
    
    return render(request,'about.html')

def Services(request):
   return render(request,'services.html')