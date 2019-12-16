from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from app_user.models import *
from .forms import RequestForm

# Create your views here.
def requests(request):
    reqs = UserRequest.objects.all()
    context ={
        'reqs' : reqs
    }
    return render(request, 'requests/requests.html', context=context)

def upload(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('requests')
        
    else:
        form = RequestForm()

    return render(request, 'requests/upload.html', {'form': form})

def delete_request(request, pk):
    if request.method == 'POST':
        reqs = UserRequest.objects.get(pk=pk)
        reqs.delete()
    return redirect('requests')
