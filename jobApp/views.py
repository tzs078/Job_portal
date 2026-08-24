from django.shortcuts import render,redirect
from jobApp.forms import RegiForm,LoginForm,RecForm,JobSeekerForm,JobPostForm
from jobApp.models import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
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

@login_required
def logoutpage(request):
     logout(request)
     return redirect('LoginPage')

@login_required
def deshboard(request):
     form = RecProfile.objects.all()
     context = {
          'form' : form,
     }
     return render(request,'pages/deshboard.html',context)


@login_required
def recPage(request):
    profile = RecProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
             form = RecForm(request.POST,instance=profile)
             if form.is_valid():
                 profile = form.save(commit=False)
                 profile.user = request.user
                 profile.save()
                 return redirect('deshboard')
     
    form = RecForm(instance=profile)
     
    context = {
             'form' : form,
             'btn' : 'Submit'
         }
    return render(request,'pages/baseForm.html',context)

@login_required
def home(request):
     form = JobSeekerProfile.objects.all()
     context = {
          'form' : form,
     }
     return render(request,'pages/home.html',context)


@login_required
def jobPage(request):
    profile = JobSeekerProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
             form = JobSeekerForm(request.POST,instance=profile)
             if form.is_valid():
                 profile = form.save(commit=False)
                 profile.user = request.user
                 profile.save()
                 return redirect('home')
     
    form = JobSeekerForm(instance=profile)
     
    context = {
             'form' : form,
             'btn' : 'Submit'
         }
    return render(request,'pages/baseForm.html',context)




@login_required
def JobPostPage(request):
    profile = JobPostModel.objects.filter(user=request.user).first()

    if request.method == 'POST':
             form = JobPostForm(request.POST,instance=profile)
             if form.is_valid():
                 profile = form.save(commit=False)
                 profile.user = request.user
                 profile.save()
                 return redirect('home')
     
    form = JobPostForm(instance=profile)
     
    context = {
             'form' : form,
             'btn' : 'Submit'
         }
    return render(request,'pages/baseForm.html',context)