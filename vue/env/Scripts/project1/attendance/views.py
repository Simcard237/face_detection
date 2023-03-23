from django.shortcuts import render
from django.http.response import StreamingHttpResponse,JsonResponse
from attendance.form import UsersForm
from datetime import datetime
from attendance.models import *
from .detecteurmouvement import VideoCamera
from django.http import HttpResponse
from time import strftime
from django.views.decorators.csrf import csrf_exempt
import pickle
import os
def gen(camera,id):
    while True:
        frame,resp = camera.get_frame(id)
        
        if resp!=1:
            att=attendance()
            if type(resp)==list:
                  att.iduser=resp[0]
                  att.date= datetime.now().strftime("%d-%m-%Y")
                  att.hours= datetime.now().strftime("%H:%M:%S")
                  att.status="present"
                  att.save()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request,id):
    path=os.getcwd().replace("\\","/")
    
    with open(path+"/static/assets/data/temp.data","rb") as file:
         fil=pickle.Unpickler(file)
         
         id=fil.load()["value"]
         user=Users.objects.filter(idt=id).first()
         
         iduser=user.id
         #except:pass   
    if id==0:
            
        if iduser:   
           return StreamingHttpResponse(gen(VideoCamera(),iduser),
                    content_type='multipart/x-mixed-replace; boundary=frame')
    else:
         return StreamingHttpResponse(gen(VideoCamera(),id),
                    content_type='multipart/x-mixed-replace; boundary=frame')   
def home(request):
    attendanc=attendance.objects.all()
    print(attendanc)
    data={"title":"", "subtitle":"","addeddate":"","Hours played":"","currently":""}
    return render(request, "index.html")

def attendancedetails(request):
    data={"title":"", "subtitle":"","addeddate":"","Hours played":"","currently":""}
    return render(request, "details.html")

def adminregister(request):
    form = UsersForm()
    print(request.method)
    if request.method=="POST":
         print(request.POST)
        
         a=request.POST["name"]
         b=request.POST["idt"]
         if not Users.objects.filter(idt=b):
             user=Users()
             user.name=a
             user.idt=b
             user.hour= datetime.now().strftime("%H:%M:%S")
             user.save()
             path=os.getcwd().replace("\\","/")
             with open(path+"/static/assets/data/temp.data","wb") as file:
                 fil=pickle.Pickler(file)
                 fil.dump({"value":request.POST["idt"]})
            

    return render(request, "browse.html",{"form":form})
def profiles(request):
    data={"title":"", "subtitle":"","addeddate":"","Hours played":"","currently":""}
    return render(request, "profile.html")

