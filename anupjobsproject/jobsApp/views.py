from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
    s='<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(s)

def delhijobsinfo(request):
    s='<h1>Delhi Jobs Information</h1>'
    return HttpResponse(s)

def lucknowjobsinfo(request):
    s='<h1>Lucknow Jobs Information</h1>'
    return HttpResponse(s)