from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.


def index(request):
    data = Blogdetails.objects.values("id")
    l = []
    l2 = []
    for i in data:
        l.append(i["id"])
    ls = set(l)
    for i in ls:
        getdata = Blogdetails.objects.filter(id=i)
        l2.append(getdata)
    Information = {"data": l2}
    return render(request, "Blog/Index.html", Information)


def blogpost(request, myid):
    Maindata = Blogdetails.objects.filter(id=myid)
    Blog = {"data": Maindata}
    return render(request, "Blog/Blogpost.html", Blog)
