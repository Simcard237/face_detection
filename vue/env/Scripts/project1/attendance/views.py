from django.shortcuts import render,redirect
from django.http.response import StreamingHttpResponse,JsonResponse
from attendance.form import UsersForm
from datetime import datetime
from django.http import HttpResponseRedirect
from attendance.models import *
from .detecteurmouvement import VideoCamera
from django.http import HttpResponse
from time import strftime
from django.views.decorators.csrf import csrf_exempt
import pickle
import os
import pandas as pd
from tkinter import filedialog
global paths
paths=os.getcwd().replace("\\","/")
def gen(camera,id,request): 
    
    resp=""
    while True:
        frame,resp = camera.get_frame(id)
        
        if resp==1 or resp==2:
            with open(paths+"/static/assets/data/temp1.data","wb") as file:
                fils=pickle.Pickler(file)
                fils.dump(resp)
            return 0    

        else:
             if type(resp)==list:
                #try:
                  print("passer 2")
                  att=attendance() 
                  if len(attendance.objects.filter(iduser=resp[0]))==0:
                    att.iduser=resp[0]
                    att.date= datetime.now().strftime("%d-%m-%Y")
                    att.hours= datetime.now().strftime("%H:%M:%S")
                    att.status=True
                    att.save()
                    with open(paths+"/static/assets/data/temp2.data","wb") as file:
                        fils=pickle.Pickler(file)
                        fils.dump(resp[0])
                        print("pass5")
                  
                  elif datetime.now().strftime("%d-%m-%Y") != attendance.objects.filter(iduser=resp[0]).values()[0]["date"]:
                           att.iduser=resp[0]
                           att.date= datetime.now().strftime("%d-%m-%Y")
                           att.hours= datetime.now().strftime("%H:%M:%S")
                           att.status=True
                           att.save()
                           with open(paths+"/static/assets/data/temp2.data","wb") as file:
                                fils=pickle.Pickler(file)
                                fils.dump(resp[0])
                                print("pass5")
                          
                          
                          
                        
                #except:pass 
                    
             yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
      

def video_feed(request,id):
    if request.method=="GET":
             print("method get pressed")
    
    if id!=1: # when it's an inscription
        iduser=0
        try:
            with open(paths+"/static/assets/data/temp.data","rb") as file:
             fil=pickle.Unpickler(file)
             id=fil.load()["value"]
             
             user=Users.objects.filter(idt=id).values()

             iduser=user[0]["id"]
            
            #except:pass   
            if iduser:
                  
                resp=gen(VideoCamera(),iduser,request)
                if resp not in [1,2]:
                    return StreamingHttpResponse(resp,content_type='multipart/x-mixed-replace; boundary=frame') 
                else:
                    form=UsersForm()
                    
                    if resp==1:
                        return render(request,"browse.html",{"form":form,"message":1})  
                    return render(request,"browse.html",{"form":form,"message":2})    
        except:pass
    else:# when it's an identification
         
         return StreamingHttpResponse(gen(VideoCamera(),id,request),
                    content_type='multipart/x-mixed-replace; boundary=frame')   
def home(request):
    attendanc=attendance.objects.all().order_by("date").order_by("hours")
    data={}
    for i in attendanc.values()[:10]:
         name=Users.objects.filter(id=i["iduser"]).values()[0]["name"]
         datatemp={"iduser":i["iduser"],"name":name,"date":i["date"],"hours":i["hours"]}
         data.update({f"{name}":datatemp})

    
    
    return render(request, "index.html",{"data":data})

def attendancedetails(request):
    attendanc=attendance.objects.all().order_by("date").order_by("hours")
    data={}
    for i in attendanc.values():
         name=Users.objects.filter(id=i["iduser"]).values()[0]["name"]
         datatemp={"iduser":i["iduser"],"name":name,"date":i["date"],"hours":i["hours"]}
         data.update({f"{name}":datatemp})

    
    
    return render(request, "details.html",{"data":data})


def profiles(request):
    data={"title":"", "subtitle":"","addeddate":"","Hours played":"","currently":""}
    return render(request, "profile.html")

def auth(request):
    if request.method=="POST":
        print(request.POST)
    return render(request, "login.html")
def generate(request):
    attendanc=attendance.objects.all().order_by("date").order_by("hours")
    data=[]
    for i in attendanc.values():
         name=Users.objects.filter(id=i["iduser"]).values()[0]["name"]
         datatemp=[i["iduser"],name,i["date"],i["hours"]]
         data.append(datatemp)
       
    
    pathf=filedialog.askdirectory(initialdir=paths,title="enter the folder path")     
    pd.DataFrame(data,columns=["iduser","name","date","hours"]).to_excel(pathf+"file.xlsx","sheet1")     
    return redirect(to="attendancedetails")
    
    