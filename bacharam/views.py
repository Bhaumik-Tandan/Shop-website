from django.http import HttpResponse
from django.shortcuts import render
from forda.models import *
from django.views.generic import ListView
c = ["Speciality", "Cake", "Sweets", "Snacks"]

p = {"head": "BACHCHARAM BAKERS", "tagline": "RISHTA WAHI SOCH NAYI",
     "category": c}
pr = Product.objects.all()


def index(request):
    d = []
    # make empy dict=
    for i in pr:
        if i.available == "n":
            continue
        a = i.category
        b = ""
        if a == "Cakes":
            b = "best"
        elif a == "Sweets":
            b = "seasonal"
        elif a == "Snacks":
            b = "other"
        l = {"name": i.name, "description": i.description, "price": i.price,
             "category": b, "recomended": i.recomended, "url": i.image.url}
        d.append(l)
    p["prod"] = d
    return render(request, "index.html", p)


class ProductList(ListView):
    model = Product


def proddet(request, pk):
    for i in pr:
        if i.name == pk:
            p["pd"] = i
            break
    return render(request, 'proddet.html', p)


def login(request):
    p["l"] = ""
    return render(request, "login.html", p)


def log(r):
    if r.method == "POST":
        l = r.POST["name"]
        pu = r.POST["password"]
        a = User.objects.all()
        for i in a:
            if (i.phone == l or i.email == l) and i.password == pu:
                return render(r, "ide.html", p)
    p["l"] = "Wrong credentials"
    return render(r, "login.html", p)


def reg(r):
    if r.method == "POST":
        print("nknjnknknk")
        n = r.POST["name"]
        e = r.POST["email"]
        pu = r.POST["phone"]
        a = r.POST["add"]
        pa = r.POST["password"]
        i = User(name=n, email=e, phone=pu, address=a, password=pa)
        i.save()
    return render(r, "ide.html", p)


def ide(request):
    p = {"head": "BACHCHARAM BAKERS", "tagline": "RISHTA WAHI SOCH NAYI"}
    return render(request, "ide.html", p)
