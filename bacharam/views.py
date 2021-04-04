from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    p = {"head": "BACHRAM BACKERS", "tagline": "RISHTA WAHI SOCH NAYI"}
    return render(request, "index.html", p)
