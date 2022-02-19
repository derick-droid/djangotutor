from django.http import HttpResponse
from django.shortcuts import render
from hello.models import Dreamreal

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

# Manipulating Data (CRUD)
def crudops(request):
    #  creating entry
    dreamreal = Dreamreal(website = "www.polo.com",  mail = "sorex@polo.com",ame = "sorex",phonenumber = "002376970")
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
