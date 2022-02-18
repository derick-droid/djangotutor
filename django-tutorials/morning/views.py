from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def good(request):
    return HttpResponse("hello good morning!")

def greet(request):
    
    return render(request, 'morning/index.html',{'name': 'derick'})
def date(request):
    today = datetime.datetime.now().date()
    return render(request, 'morning/date.html', {'today':today})
def displayfor(request):
    daysweek = ["monday", "tuesday", "wednesday", "thursday", "friday","saturday", "sunday"]
    return render(request, 'morning/for.html', {'daysweek': daysweek})