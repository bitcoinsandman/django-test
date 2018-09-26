from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Congrats. Here's your directory")

def objectives(request):
    return HttpResponse("Objectives Page...")

def profile(request, collegeName):
    return HttpResponse("You're viewing " + collegeName + "'s profile")