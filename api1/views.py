from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def main1(request,name):
    return HttpResponse(f'<h1>Hi- {name}</h1>')


def index(request):
    return HttpResponse("<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores corrupti maxime error molestias magnam fuga iste amet, exercitationem dolorem odit!</p>")