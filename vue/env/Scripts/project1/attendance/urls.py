
from django.urls import path,include
from .views import *
urlpatterns = [
     path("",home, name="home"),
     path("attendancedetails/",attendancedetails, name="attendancedetails"),
     path("register/",adminregister, name="adminregister"),
     path("profiles/",profiles, name="profiles"),
     path("streaming/<int:id>",video_feed,name="stream"),
  
    
]
