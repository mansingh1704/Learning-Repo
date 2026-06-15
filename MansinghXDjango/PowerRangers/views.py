from django.shortcuts import render
from .models import RangerTypes ,RangerStores
from django.shortcuts import get_object_or_404
from .forms import RangerTypesForm

# Create your views here.

def all_rangers(request):
    rangers = RangerTypes.objects.all()
    return render(request, 'ranger/all_rangers.html', { 'rangers': rangers})


def ranger_store_view(request):
    stores = None

    # submitting the form
    if request.method == 'POST':
        form = RangerTypesForm(request.POST)
        if form.is_valid():
            ranger_types = form.cleaned_data['ranger_type']
            stores = RangerStores.objects.filter(ranger_type_available= ranger_types)
    else:
        form = RangerTypesForm()   


    return render(request, 'ranger/ranger_stores.html', {'stores': stores, 'form':form})