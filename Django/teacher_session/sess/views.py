from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.
"""

class StudentListView(ListView):
    queryset = Student.objects.all().filter(gender="man")
    template_name = "student_list.html"

def mySess(req):
    print(type(req.session))
    print(req.session.get("teacher_name", "NoName"))

    req.session.clear()
    req.session["teacher_name"] = "Jich"
    print(req.session)
    del req.session["teacher_name"]
    print("My Sess")
    return None

def student(req):
    stus = Student.objects.all()
    p = Paginator(stus, 40)
    print(p.count)
    print(p.num_pages)
    print(p.page_range)

    p.page(3)
"""





