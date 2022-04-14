from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    text = '<h1> Hello welcome to my blog </h1>'
    return HttpResponse(text)