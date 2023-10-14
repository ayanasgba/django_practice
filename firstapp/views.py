from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
# def index(request):
#     return render(request,"firstapp\home.html")
def index(request):
    return TemplateResponse(request,"firstapp/home.html")
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