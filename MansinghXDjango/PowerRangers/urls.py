 # copy paste all this code from main project folder's urls.py


from django.contrib import admin
from django.urls import path
from . import views  #importing views.py from current directory


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeMansingh, name="Home | Mansingh"), 
    path('aboutMansingh/', views.aboutMansingh, name="About| Mansingh"), 
    path('connectMansingh/', views.connectMansingh, name="Connect | Mansingh"),
    path('')
    
]
