# copy paste all this code from main project folder's urls.py


from django.urls import path
from . import views  #importing views.py from current directory

#localhost:8000/PowerRangers
urlpatterns = [
    path('', views.all_rangers, name="All Power Rangers"), 
        
]
