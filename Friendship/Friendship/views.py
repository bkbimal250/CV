
from re import template
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
