from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),

    path('', views. index),
    re_path(r'^about', views.about),
    re_path(r'^contact', views .contact),
]