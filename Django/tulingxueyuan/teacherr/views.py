from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def do_normalmap(request):
    return HttpResponse("This is normalmap")

def withparam(request, year, month):
    return HttpResponse("The params is year {0} month {1}".format(year, month))

def do_app(request):
    return HttpResponse("这是teacher路由")

def do_param2(request, pn):
    return HttpResponse("The param is : {0}".format(pn))

def do_extemParam(request,name):
    return HttpResponse("My name is : {0}".format(name))

def recParse(request):
    return HttpResponse("Your URL is : {0}".format(reverse("askname")))