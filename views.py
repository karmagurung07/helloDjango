from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
	return HttpResponse('Hello, World! I am Karma Gurung and this is my first Django Project')

