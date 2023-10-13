from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World! Это мой первый проект на Django!")
def about(request):
    return HttpResponse("<h2>0 сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid = 1):
    output = "<h2>Продукт- № {0}</h2>".format(productid)
    return HttpResponse(output)
def users(request, id, name):
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(id,name)
    return HttpResponse(output)