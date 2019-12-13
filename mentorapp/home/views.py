from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')



# Request as argument:
# When a page is requested, Django creates an HttpRequest object that contains metadata about the request.
# Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.
# Each view is responsible for returning an HttpResponse object


# Response as argument:
# In contrast to HttpRequest objects, which are created automatically by Django, HttpResponse objects are your responsibility.
# Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
#
# The HttpResponse class lives in the django.http module.
