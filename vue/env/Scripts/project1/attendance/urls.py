
from django.urls import path,include
from .views import *
urlpatterns = [
     path("",home, name="home"),
     path("attendancedetails/",attendancedetails, name="attendancedetails"),
     path("register/",include("api.urls")),
     path("profiles/",profiles, name="profiles"),
     path("streaming/<int:id>",video_feed,name="stream"),
     path("signin/", auth, name="signin"),
     path("checking/", include("api2.urls")),
     path("generate/", generate,name="generate")
     
    
] 
