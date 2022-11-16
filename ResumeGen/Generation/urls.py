from django.contrib import admin
from django.urls import path,include
from Generation import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('create',views.create, name='create'),
    path('testing',views.testing, name='testing'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact')
]
