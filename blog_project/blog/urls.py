from .views import about,home, login_view
from .forms import SignUpForm 
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_view,name='log-in'),
    path('about/',login_required(about),name='blog-about'),
    path('home/',login_required(home),name='blog-home')


]       