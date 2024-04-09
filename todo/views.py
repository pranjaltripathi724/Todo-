from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse


def user_signup(request):
    if request.method=='GET':
        form=UserCreationForm()
        return render(request,"signup.html",{"form":form})
    else:
        user=UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/login/')        


def user_login(request):
    form=request.POST
    if request.method == 'POST':
        username = form['username']
        password = form['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/one/')
        else:
            return redirect('/login/')
    return render(request,"login.html")        


def user_logout(request):
    logout(request)
    return redirect('/login')


@login_required(login_url="/login/")
def one(request):
    data=list(models.Todo.objects.all().values())
    return render(request,"first.html",{"data":data})

@login_required(login_url="/login/")
def addtask(request):
    data=dict(request.GET)
    # id=int(data['id'][0])
    task=data['task'][0]
    data_one=models.Todo(task=task)
    data_one.save()
    data=list(models.Todo.objects.all().values())
    return render(request, "first.html",{'data':data})

@login_required(login_url="/login/")
def delete(request,id):
    pro=models.Todo.objects.get(id=id)
    pro.delete()
    data=models.Todo.objects.all().values()
    return render(request,"first.html",{"data":data})

@login_required(login_url="/login/")
def show(request):
    data=list(models.Todo.objects.all().values())
    return render(request,"first.html",{"data":data})

@login_required(login_url="/login/")
def edit(request,id):
    data=models.Todo.objects.get(id=id)
    if request.method == 'POST':
        data.task=request.POST.get('task')
        data.save()
        return redirect('/show/')
    return render(request,"edit.html",{"data":data})    

