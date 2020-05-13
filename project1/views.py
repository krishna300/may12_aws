
from django.shortcuts import HttpResponse

def main(request):
    return HttpResponse('<h1>Hi manu-chand</h1>')



def hello(request):
    return HttpResponse('<h1>Hello  I am from Dangal !!</h1>')