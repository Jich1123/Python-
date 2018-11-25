from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def teacher(r):
    return HttpResponse("这是TEACHER的视图")

def v2_exception(r):
    raise Http404
    return HttpResponse("OK")

def v10_1(r):
    return HttpResponseRedirect("/v11")

def v10_2(r):
    return HttpResponseRedirect(reverse("v11"))

def v11(r):
    return HttpResponse("哈哈！这是V11返回的内容")

def v8_get(req):
    rst = ""
    for k,v in req.GET.items():
        rst += k + "-->" + v + ","

    return HttpResponse("Get value of Request is {0}".format(rst))

def v9_get(req):
    return render_to_response("for_post.html")

def v9_post(req):
    rst = ""
    for k,v in req.POST.items():
        rst += k + "-->" + v + ","

    return HttpResponse("Get value of POST is {0}".format(rst))

def render_test(request):
    rsp = render(request, "render.html")
    return rsp

def render2_test(request):
    c = dict()
    c["name"] = "Jich"
    rsp = render(request, "render2.html", context=c)
    return rsp

def render3_test(request):
    from django.template import loader
    t = loader.get_template("render2.html")
    print(type(t))
    r = t.render({"name":"Jich"})
    print(type(r))
    return HttpResponse(r)

def render4_test(request):
    return render_to_response("render2.html", context={"name":"Jich"})

def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request, template_name="page404.html")