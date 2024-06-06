from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    return render(req, 'wsite/index.html', {'title': 'mytitle'})
