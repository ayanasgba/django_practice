from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from django.views.generic import TemplateView


urlpatterns = [
    # path('', views.index, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),

    path('', views. index),
    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html",
                                          extra_context={"work":"Helllllooooo, it is my work!"})),
    path('details/', views.details),

    # re_path(r'^about', views.about),
    # re_path(r'^contact', views .contact),

    # re_path(r'^products/$', views.products),
    # re_path(r'^products/(?P<productid>\d+)/', views.products),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    # path('products/', views.products),

    # path('products/<int:productid>/', views.products),
    # path('users/', views.users),

    # path('users/<int:id>/<str:name>/', views.users),
]