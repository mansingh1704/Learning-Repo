from django.shortcuts import render
from .models import RangerTypes

# Create your views here.

def all_rangers(request):
    rangers = RangerTypes.objects.all()
    return render(request, 'ranger/all_rangers.html', { 'rangers': rangers})