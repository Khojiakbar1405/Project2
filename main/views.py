from django.shortcuts import render
from django.http import HttpResponse
# from .models import *


def main(request):
    
    return render(request, 'index.html') 
