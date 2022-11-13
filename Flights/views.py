from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Availability,Airline
from django.http import HttpResponse
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
    if request.method=='POST':
        datei=request.POST.get('datef')
        timei=request.POST.get('timef')
        srci=request.POST.get('source')
        desti=request.POST.get('destination')
        adc=request.POST.get('adults')
        chc=request.POST.get('children')
    if datei is not None and timei is not None and srci is not None and desti is not None:
        flights_available=Availability.objects.filter(date=datei).filter(src=srci).filter(dest=desti)


    context={'flights_available':flights_available,}
    return render(request,'available.html',context)
def admina(request):
    return redirect('admina')
