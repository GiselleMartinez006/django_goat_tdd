from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>To-Do lists </title> <body><h1>Workingx3</h1> </body> </html>')
                            



# Create your views here.
