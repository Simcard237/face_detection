from django.shortcuts import render,redirect
from django.http.response import StreamingHttpResponse,JsonResponse
from attendance.form import UsersForm
from datetime import datetime
from django.http import HttpResponseRedirect
from attendance.models import *
from time import strftime
import pickle
import os
# Create your views here.

def checking(request):
    return render(request, "checking.html")

def testapi(request):
   path=os.getcwd().replace("\\","/") 
   fils=""
   try:
    with open(path+"/static/assets/data/temp2.data","rb") as file:
                fil=pickle.Unpickler(file).load()
                print("etape 1 ", fil)     
                fils=attendance.objects.filter(iduser=fil).values()[0]
    with open(path+"/static/assets/data/temp2.data","wb") as file:
         pass          
   
   except:pass
   if fils!="":
      user=Users.objects.filter(id=fils["iduser"]).values()[0]["name"]
      data={"message":1,"iduser":fils["iduser"], "name":user.upper(),"date":fils["date"],"hours":fils["hours"],}
        
      return JsonResponse(data,status=201)
   return JsonResponse({"message":0},status=201) 