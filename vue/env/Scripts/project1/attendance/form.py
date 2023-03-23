from django.forms import ModelForm, CharField,TextInput
from .models import *

# Create the form class.
class UsersForm(ModelForm):
     
     name = CharField(widget=TextInput(attrs={'class': 'myfieldclass','style':"width:50%;background-color: dimgrey;color: white;", 'placeholder':"Enter the Name of the User","id":"field1" }),max_length=50)
     idt = CharField(widget=TextInput(attrs={'class': 'myfieldclass','style':"width:50%;background-color: dimgrey;color: white;", 'placeholder':"Enter the Id of the User","id":"field2"  }),max_length=20)
     class Meta:
         model = Users
         fields = ['name', 'idt']
     


# Creating a form to add an Users.
