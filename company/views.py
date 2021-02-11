from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .form import *
from django.utils import timezone
from django.http import HttpResponse , HttpResponseRedirect


# Create your views here.


def home(request):
    return render(request,'base.html')


def index(request):
    return render(request,'index.html')


def blockchain(request):
    return render(request,'new.html')

@login_required(login_url="login")
def employee(request):
    obj = Employee.objects.all()
    myform = NewEmp()
    if request.method == 'POST' :
        myform = NewEmp(request.POST)
        if myform.is_valid():
            myform.save()
        myform = NewEmp()
    return render(request,'employee.html',{'obj':obj,'myform':myform})

@login_required(login_url="login")
def department(request):
    dept=Department.objects.all()
    myform = NewDept(request.POST)
    if myform.is_valid():
        myform= myform.save()
        myform = NewDept()

    return render(request,'department.html',{'dept':dept,'myform':myform})

















