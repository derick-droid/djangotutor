from django.http import HttpResponse
from django.shortcuts import redirect, render
from hello.models import Dreamreal

# http response
def welcome(request):
    text = "<h1> welcome to my app </h1>"
    return HttpResponse(text)
# rendering html page
def home(request):
    return render(request, "hello/index.html")

def hope(request):
    return render(request, "hello/hope.html")

def diva(request):
    return render(request, "hello/diva.html")

# views accepting parameters

def name(request, name):
    return HttpResponse(f"hello,{name.capitalize()}")

# Manipulating Data (CRUD)
def crudops(request):
    #  creating entry
    dreamreal = Dreamreal(website = "www.polo.com",mails = "sorex@polo.com", name = "sorex")
    dreamreal.save()
    
    # read all entries
    objects  = Dreamreal.objets.all()
    res = "printing all Dreamreal entries in DB: <br> "
    for elt in objects:
        res += elt.name + "<br>"
        
    #  read a specific entry
    
    sorex = Dreamreal.objects.get(name = "sorex")
    res += "printing one entry <br> "
    res += sorex.name
    #  delete an entry
    res+= "<br> Deleting an entry <br>"
    sorex.delete
    
    # update 
    dreamreal = Dreamreal(website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970")
    
    dreamreal.save()
    res+= "updating entry <br> "
    dreamreal = Dreamreal.objects.get(name = "sorex")
    dreamreal = "thierry"
    dreamreal.save()
    return HttpResponse(res)

#  further page redirection
def page(request):
    flag = False
    if flag == True:
        
         return redirect("/hello/home/")
    else:
        return redirect("/hello/welcome/")
        
   
#  another redirect
def studios(request):
    Q = request.GET.get('q')
    
    if Q == str(1):
        return redirect("/hello/hope/")
    elif Q == str(0):
        return redirect("/hello/diva/")
    
    else:
        return HttpResponse("<h1> NOT AVAILABLE COMMAND</h1>")
        