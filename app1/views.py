from django.shortcuts import render, HttpResponse,redirect

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
        
        print(username,email,password1,password2)
    return render(request,'signup.html')
