from django.shortcuts import render

# To call the view, we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the mentorsearch directory, create a file called urls.py.

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the mentorsearch index.")



