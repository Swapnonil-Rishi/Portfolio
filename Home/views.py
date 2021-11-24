from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# from home.models import Destination
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def Home(request):
   
    if request.user.is_authenticated:
        # Foods=Destination.objects.all()
        return render(request,"index.html")
    else:
        return redirect("/login")
def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("/login")
    return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            # if User.objects.filter(username=None,email=None).exists():
            #     messages.info(request, 'you missed something')
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, 'Email taken')
            #     return redirect('/accounts/register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, last_name=last_name, first_name=first_name, email=email)
                user.save()
                messages.success(request, 'Log in please')
                return redirect('/')
        else:
            messages.info(request, 'Password is not matching')
        return redirect('/register')
    else:
        return render(request, 'register.html')



def Logout(request):
    logout(request)
    return redirect("/login")