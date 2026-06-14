from django.shortcuts import render
from .models import RangerTypes
from django.shortcuts import get_object_or_404

# Create your views here.

def all_rangers(request):
    rangers = RangerTypes.objects.all()
    return render(request, 'ranger/all_rangers.html', { 'rangers': rangers})