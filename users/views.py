from django.shortcuts import render,redirect,get_object_or_404  
from django.urls import reverse
from .forms import LoginForm,SignupForm
from django.contrib.auth import  authenticate,login,logout
from django import forms

# django forms
def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))   
    next1 = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        if username and password is not None:
            user = authenticate(username=username,password=password)
            login(request,user)
            if next1:
                return redirect(next1)
        return redirect(reverse('discover:index'))
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def signupView(request):
    form = SignupForm(request.POST or None, request.FILES or None)
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))
    if form.is_valid():
        user =form.save(commit= False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username=user.username, password=password)
        login(request, user)
        if user.userType == 'Regular user':
            return redirect(reverse('profiles:reguser'))
        else:
            return redirect('profiles:duser')
    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)

def logoutView(request):
    logout(request)
    return redirect(reverse('home:index'))
