from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    p = {"head": "BACHCHARAM BAKERS", "tagline": "RISHTA WAHI SOCH NAYI"}
    return render(request, "index.html", p)


def ide(request):
    p = {"head": "BACHCHARAM BAKERS", "tagline": "RISHTA WAHI SOCH NAYI"}
    return render(request, "ide.html", p)
