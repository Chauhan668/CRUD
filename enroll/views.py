from ast import Import
import email
from unicodedata import name
from django.shortcuts import render , HttpResponseRedirect
from .models import User

from enroll.models import User
from .forms import StudentRegistrations

# Create your views here.


#This function add all items and show items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)  
            reg.save()
            fm = StudentRegistrations()
    else:
        fm = StudentRegistrations()
    Stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':Stud})

# This functionn will update and edit.
def update_data(request ,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistrations(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistrations(instance=pi)
    return render(request, 'enroll/updatestudents.html',{'form': fm}) 


# This fucntion will delete items

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')