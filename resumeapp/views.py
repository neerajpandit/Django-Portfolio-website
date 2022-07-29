from django.shortcuts import render

# Create your views here.
from email import message
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        new_emp=Contact(name=name,email=email,subject=subject,message=message)
        new_emp.save()
    return render(request,'resumeapp/index.html')
