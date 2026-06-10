from django.http import HttpResponse  #this sends the response what we have to send or show to the client
from django.shortcuts import render


# Now we make methods for different things which can be named differently
# like mansinghhome, nagraj, billu etc etc

# format---> return render(request, path/name of the html file)

def homeMansingh(request):
    # return HttpResponse("Hello World, Welcome to the home page of MansinghAndDjango")
    return render(request, 'website/index.html')  #this render will load the file on  webpage

def aboutMansingh(request):
    # return HttpResponse("This the about page of MansinghAndDjango")
    return render(request, 'website/about.html')

def connectMansingh(request):
    # return HttpResponse("This is the Contacts and Connection page of Mansingh And Django")
    return render(request, 'website/connect.html')