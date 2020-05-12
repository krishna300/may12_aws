from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def main1(request,name):
    return HttpResponse(f'<h1>Hi- {name}</h1>')