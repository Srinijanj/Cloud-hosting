from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


# DRF API View
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Pages

def home(request):
    return render(request, 'store/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def registered_users(request):
    from django.contrib.auth.models import User
    users = User.objects.all()
    return render(request, 'store/registered_users.html', {'users': users})


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image
        )
        return redirect('store')

    return render(request, 'store/add_product.html')


def store(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})
from django.shortcuts import render

def store_home(request):
    return render(request, 'store/store.html')
