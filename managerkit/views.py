from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def manager(request):
    return render(request, 'home.html')\
    #Testing