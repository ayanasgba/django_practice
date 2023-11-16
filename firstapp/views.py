from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    # data = {"age": 66}
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    return render(request,"firstapp/index.html", context={'cat': cat})
#     data = {"header":"Передача параметров в шаблон",
#             "message":"Шаблон загружен в index_app1.html"}
#     return render(request,"firstapp/index_app1.html", context=data)

# def index(request):
#     header = "Персональные данные"  # обычная переменная
#     langs = ["Английский", "Немецкий", "Испанский"]  # массив
#     user = {"name": "Максим,", "age": 30}  # словарь
#     addr = ("Виноградная", 23, 45)  # кортеж
#     data = {"header": header, "langs": langs, "user": user, "address": addr}
#     return TemplateResponse(request,"index.html", data)

def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")

# def products(request, productid = 1):
#     output = "<h2>Продукт- № {0}</h2>".format(productid)
#     return HttpResponse(output)

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)

# def users(request, id=1, name="Ayane"):
#     output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(id,name)
#     return HttpResponse(output)

def users(request):
    id = request.GET .get("id", 1)
    name = request.GET.get("name", "Ayane")
    output = "<h2>Пользователь</h2><hЗ>id: {0} Имя: {1}</hЗ >".format(id, name)
    return HttpResponse(output)