from django.urls import path,include
from .views import *
urlpatterns = [
  
      path("", checking, name="checking"),
      path("testapi/", testapi, name="testapi"),
]
     
    