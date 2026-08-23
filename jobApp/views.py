from django.shortcuts import render,redirect
from jobApp.forms import RegiForm,LoginForm
from jobApp.models import *
from django.contrib.auth import login,logout
# Create your views here.
def regiPage(request):

    if request.method == 'POST':
        form = RegiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginPage')

    form = RegiForm()

    context = {
        'form' : form,
        'btn' : 'Register'
    }
    return render (request,'pages/baseForm.html',context)


def LoginPage(request):
    if request.method == 'POST':
            form = LoginForm(request,request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)          
                return redirect('deshboard')
    
    form = LoginForm()
    
    context = {
            'form' : form,
            'btn' : 'Login'
        }
    return render (request,'pages/baseForm.html',context)


def deshboard(request):
     return render(request,'pages/deshboard.html')