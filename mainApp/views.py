from django.shortcuts import render

# Create your views ehere.
def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html' , {'values' : [ 'text you' ,'234'] })
