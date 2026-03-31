from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *


def register_view(request):
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})
    

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import redirect

def dashboard_view(request):
   if request.user.role == 'candidate':
       return redirect('candidate_dashboard')
   elif request.user.role == 'recruiter':
       return redirect('recruiter_dashboard')
   else:
       return redirect('/admin')

#    return render(request, 'accounts/dashboard.html')


def home_view(request):
    return render(request, 'accounts/main.html')
