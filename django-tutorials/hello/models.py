from operator import mod
# from tkinter import CASCADE
from unicodedata import name
from django.db import models

class Dreamreal(models.Model):
    website = models.CharField(max_length=50)
    mails = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phonenumber = models.IntegerField
    online = models.ForeignKey('Online', on_delete=models.CASCADE)
    
    
    class meta:
        db_table = "dreamreal"
        
        
class Online(models.Model):
    domain = models.CharField(max_length=30)
    
    class meta:
        dt_table = "online"
        
        
    