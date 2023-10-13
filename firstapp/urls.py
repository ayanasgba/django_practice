from django.contrib import admin
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),

    path('', views. index),
    re_path(r'^about', views.about),
    re_path(r'^contact', views .contact),
    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productid>\d+)/', views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
]