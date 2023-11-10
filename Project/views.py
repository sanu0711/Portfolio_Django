from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def allprojects(request):
   return render(request, '../templates/allprojects.html')
def tests(request):
    return HttpResponse("This is a test page")
