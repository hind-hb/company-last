from django.shortcuts import render,redirect
from .form import SignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')

    return render (request,'signup.html',{'form':form})