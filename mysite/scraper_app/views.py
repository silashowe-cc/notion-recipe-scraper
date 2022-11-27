from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# These are used to return something to a http request To map them, we also need to set up something with URLs

def index (request):
    return HttpResponse("hello world")
