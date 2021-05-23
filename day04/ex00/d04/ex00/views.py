from django.shortcuts import render
#from django.http import HttpResponse

def ex00_page(request):
    response = render(request, 'index.html')
    return response
