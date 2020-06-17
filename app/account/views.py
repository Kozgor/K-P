from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from apartments.models import Apartments


def login(request):
    data = {"header_h1": "Вхід",
            "header_p": "Головна >> Вхід"}
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User logged')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login or password!')
            return redirect('login')
    else:
        return render(request, 'account/login.html', context=data)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['Name']
        last_name = request.POST['Surname']
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists!")
                return redirect("register")
            if User.objects.filter(email=email).exists():
                messages.error(request, "This email already exists!")
                return redirect("register")
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            messages.success(request, "Success! Now you can log in!")
            return redirect('login')
        else:
            messages.error(request, "Passwords not match!")
            return redirect('register')
    data = {"header_h1": "Реєстрація",
            "header_p": "Головна >> Реєстрація"}
    return render(request, 'account/register.html', context=data)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Successfully logged out!")
    return redirect('index')


def dashboard(request):
    return render(request, 'account/dashboard.html')
