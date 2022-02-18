from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# http response
def welcome(request):
    text = "<h1> welcome to my app </h1>"
    return HttpResponse(text)
# rendering html page
def home(request):
    return render(request, "hello/index.html")

# views accepting parameters

def name(request, name):
    return HttpResponse(f"hello,{name.capitalize()}")
