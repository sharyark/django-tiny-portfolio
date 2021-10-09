from re import L
from django import http
from django.shortcuts import render
# from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import Post
# from django.contrib.auth.forms import UserCreationForm
from .forms import editing, singup_,login_
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request,'blog/home.html',{'post':post})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
        return render(request,'blog/contact.html')
def dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        return render(request,'blog/dashboard.html',{'post':post})
    else:
        return HttpResponseRedirect('/login')
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = login_(request=request, data=request.POST)
            if form.is_valid():
                nm = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                user = authenticate(username=nm,password=pw) 
                if user is not None:
                    login(request, user)
                    messages.success(request,'logged in successfully')
                    return HttpResponseRedirect('/dashboard')
        else:
            form = login_()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard')

def singup(request):
    if request.method == 'POST':
        form = singup_(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = singup_()
    return render(request,'blog/signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def delete(request,id):
    if request.method == 'POST':
        # dl = user()
        dl = Post.objects.get(pk=id)
        # print(dl.id)
        dl.delete()
        print('deleting is working')
    return HttpResponseRedirect('/')
def editt(request,id):
    # form = editing()
    # obj = Post.objects.get(pk=id)

    # return render(request,'blog/editing.html',{'form':form})

    if request.method == 'POST':
        obj = Post.objects.get(pk=id)
        form = editing(request.POST)
        if form.is_valid():
            ti = form.cleaned_data['title']
            des = form.cleaned_data['desc']
            # new_obj = Post(title = ti, desc= des)
            obj.title = ti
            obj.desc = des
            obj.save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = editing()
    return render(request,'blog/editing.html',{'form':form})