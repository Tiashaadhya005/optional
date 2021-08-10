from .models import User_lists
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth


#from models import user_list
# Create your views here.
arr={}
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method =='POST':
        Firstname=request.POST.get('Firstname','')
        Lastname=request.POST.get('Lastname','')
        Email=request.POST.get('email','')
        Username=request.POST.get('username','')
        password=request.POST.get('password','')
        arr[Username]= password
        u=User_lists(Username=Username, Password=password, Email=Email, Firstname=Firstname, Lastname=Lastname)
        u.save()
        #print('Saved!')
        messages.info(request,"Successfully Registered")
        return redirect('/')
    else:return render(request,"register.html")

def login(request):
    if request.method=='POST':
        Username= request.POST.get("Username","")
        Password= request.POST.get("Password","")
        u=User_lists.checkss(Username,Password)
        if u==True :
            messages.info(request, 'Login Successful')
            return redirect('/')
        else:
            #return HttpResponse("invalid login")
            messages.info(request,"Invalid login")
            return render(request,'login.html')

    else:return render(request,"login.html")