from django.shortcuts import render,redirect
from django.http.response import StreamingHttpResponse,JsonResponse
from attendance.form import UsersForm
from datetime import datetime
from django.http import HttpResponseRedirect
from attendance.models import *

from django.http import HttpResponse
from time import strftime
from django.views.decorators.csrf import csrf_exempt
import pickle
import os
# Create your views here.
def testapi(request):
   path=os.getcwd().replace("\\","/") 
   fils=""
   try:
    with open(path+"/static/assets/data/temp1.data","rb") as file:
                fils=pickle.Unpickler(file).load()     
    with open(path+"/static/assets/data/temp1.data","wb") as file:
        pass
    
   except:pass
   if fils!="":
    return JsonResponse({"message":fils},status=201)
   return JsonResponse({"message":0},status=201) 
def adminregister(request):
    form = UsersForm()
    
    if request.method=="POST":
         a=request.POST["name"]
         b=request.POST["idt"]
         if len(Users.objects.filter(idt=b).values())==0:
             user=Users()
             user.name=a
             user.idt=b
             user.hour= datetime.now().strftime("%H:%M:%S")
             user.save()
             path=os.getcwd().replace("\\","/")
             with open(path+"/static/assets/data/temp.data","wb") as file:
                 fil=pickle.Pickler(file)
                 fil.dump({"value":request.POST["idt"]})
             return render(request, "browse.html",{"form":form, "message":1})    
         elif len(Users.objects.filter(idt=b).values())>0:
             return render(request,"browse.html",{"form":form,"message":2})  
   

            
   
    return render(request, "browse.html",{"form":form, "message":0})
   
        