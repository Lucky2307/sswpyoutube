from django.shortcuts import render, redirect, reverse

def index(request):
    if request.user.is_authenticated:
        return redirect('videos-index')
    else:
        return redirect('landingpage')