from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(req):
    return render(req, template_name="one.html")
def two(req):
    ct = dict()
    ct["name"] = "Jich"
    return render(req, template_name="two.html", context=ct)
def three(req):
    ct = dict()
    ct["score"] = [99,98,87,96]
    return render(req, template_name="three.html", context=ct)
def four(req):
    ct = dict()
    ct["name"] = "Jich111"
    return render(req, template_name="four.html", context=ct)
def five_get(req):
    return render(req, template_name="five_get.html")
def five_post(req):
    print(req.POST)
    return render(req, template_name="one.html")
