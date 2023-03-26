
from django.urls import path,include
from .views import *
urlpatterns = [
  
     path("",adminregister, name="adminregister"),
     path("testapi/", testapi, name="testapi"),
]
     
    