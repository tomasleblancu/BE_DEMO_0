from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import *

# Create your views here.

def Index(request):

    context = {}
    
    return render(request, 'index/index.html', context)

def Servicios(request):

    context = {}
    
    return render(request, 'pages/servicios.html', context)

def Contacto(request):

    context = {}
    
    return render(request, 'pages/contacto.html', context)

##Login y registro
def Login(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            
            else:
                print('error')
                messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}

    return render(request, 'user/login.html', context)

def Register(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                
                form.save()

                return redirect('index')          

    context = {'form':form}

    return render(request, 'user/register.html', context)

@login_required(login_url='login')
def Logout(request):

    logout(request)

    return redirect('index')