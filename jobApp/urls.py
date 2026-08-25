from django.urls import path
from jobApp.views import *
urlpatterns = [
    path('',regiPage,name = 'regiPage'),
    path('LoginPage',LoginPage,name='LoginPage'),
    path('logoutpage',logoutpage,name='logoutpage'),

    path('deshboard',deshboard,name='deshboard'),
    path('home',home,name='home'),
    
    path('recPage',recPage,name='recPage'),
    path('jobproPage',jobproPage,name='jobproPage'),

    path('JobPostPage',JobPostPage,name='JobPostPage'),
    path('jobPage',jobPage,name='jobPage'),
    path('JobApplyPage',JobApplyPage,name='JobApplyPage'),
]