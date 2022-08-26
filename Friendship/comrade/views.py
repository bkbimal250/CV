
from re import template
from unicodedata import name
from django.shortcuts import render, redirect
# from .forms import userForm

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


# Create your views here.

def Home(request):
    
    return render(request,'index.html')

def About(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")
    

def blog(request):
    return render(request,"blogs.html")

def Baapsab(request):
    return render(request,"Baapsab.html")

def login(request):
    
    try:
        
        if request.method=="post":
            n1=request.Post.get['email']
            n2=request.Post.get['psw']
            print(n1," ",n2)
        return render(request,'login.html')
        
        
        
    except:
        pass
    
        return render(request,"login.html")
    
  

def news(request):
    return render(request,"news.html")

def Calculator(request):
    c=''
    
    
    try:
        if request.method=="POST":
            
            n1=eval(request.POST.get('value1'))
            n2=eval(request.POST.get('value2'))
            
            opr=request.POST.get('opr')
            
            if opr=='+':
                c=n1+n2
            elif opr=='-':
                c=n1-n2
                
            elif opr=='*':
                c=n1*n2
                
            elif opr=='/':
                c=n1/n2
            
                
            
        
        
    except:
        c='input number into correct form'
        print(c)
    print(c)
    return render(request,"calculator.html",{'c':c})


def Evenodd(request):
    
    d=''
    
        
    if request.method=="POST":
            if request.POST.get('number')=='' and request.POST.get('number')=='a':
                return render(request,"evenodd.html",{'error':True})
                
                
            num=eval(request.POST.get('number'))
            
            if num%2==0:
                d="Even number"
                return render(request,"evenodd.html",{'d':d})
        
                
            else:
                d="Odd number"
                return render(request,"evenodd.html",{'d':d})
                
        
    





    


