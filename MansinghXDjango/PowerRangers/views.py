from django.shortcuts import render

# Create your views here.

def all_rangers(request):
    return render(request, 'rangers/all_rangers.html')