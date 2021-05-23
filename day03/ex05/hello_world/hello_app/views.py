from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    return HttpResponse('Hello World!')