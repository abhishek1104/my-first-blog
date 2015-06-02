from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world! <br/> <a href='/about2/'>About2</a>")


   