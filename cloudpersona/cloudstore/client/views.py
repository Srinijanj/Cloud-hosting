
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('client_login')
    return render(request, 'client/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client_store')
        else:
            return render(request, 'client/login.html', {'error': 'Invalid credentials'})
    return render(request, 'client/login.html')

from django.shortcuts import redirect

def redirect_to_store(request):
    return redirect('store')

from django.shortcuts import render
from django.contrib.auth.models import User  # Django’s built-in user model



