from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('This is First String')

def string2(request):
    return HttpResponse('This is Second String')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

    
