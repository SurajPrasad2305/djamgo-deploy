from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from app.views import *

# def home(request):
#     print('hello world this is home')
#     return HttpResponse('hello')

urlpatterns = [
    path('',home,name='home' ),
    path('login',login,name='login'),
    path('signup',signup),
    path('doctors',doctors,name = 'doctors'),
    path('logout',signout,name='logout')

]
