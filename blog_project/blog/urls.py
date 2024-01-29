from .views import about,home
from .forms import SignUpForm 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',home,name='blog-home'),
    path('about/',about,name='blog-about')

]       