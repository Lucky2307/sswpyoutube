from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator

def footer(request):
    return render(request, 'footer/help.html')
def footer2(request):
    return render(request, 'footer/about.html')

    