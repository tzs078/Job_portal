from django.urls import path
from jobApp.views import *
urlpatterns = [
    path('',regiPage,name = 'regiPage'),
    path('LoginPage',LoginPage,name='LoginPage'),
    path('deshboard',deshboard,name='deshboard'),
]