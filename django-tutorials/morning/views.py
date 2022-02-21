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
#  page redirect

def redirect(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "morning/index.html", {"today" : today, "days_of_week" : daysOfWeek})


def viewArticle(request, articleId):
   """ A view that display an article based on his ID"""
   text = "Displaying article Number : %s" %articleId
   return HttpResponse(text)


