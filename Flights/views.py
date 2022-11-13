from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Availability,Airline
# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'osignup.html',context)
@login_required
def home(request):
     return render(request,'home.html')
def loginPage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context={}
    return render(request,'osignin.html',context)
def logOutUser(request):
    logout(request)
    return redirect('loginPage')
def base(request):
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')

def available(request):
    model=Availability
    flights_available=Availability.objects.all()
    context={'flights_available':flights_available,}
    return render(request,'available.html',context)
