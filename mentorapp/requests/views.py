from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from app_user.models import *
from .forms import RequestForm
from helper import parse_req_body

# Create your views here.
def requests(request):
    user = request.user
    if user.is_authenticated:
        if user.is_student:
            reqs = UserRequest.objects.get(student=user)
        elif user.is_mentor:
            reqs = UserRequest.objects.get(mentor=user)
        context ={
            'reqs' : reqs
        }
        return render(request, 'requests/requests.html', context=context)
    else:
        return redirect('home')

def upload(request):
    user = request.user
    if user.is_authenticated:
        if user.is_student:
            if request.method == 'POST':
                form = RequestForm(request.POST, request.FILES)
                if form.is_valid():
                    form.student = request.user
                    form.save()
                    return redirect('requests')
            else:
                form = RequestForm()
            return render(request, 'requests/upload.html', {'form': form})
        else:
            return redirect('requests')
    else:
        return redirect('home')

def delete(request, pk):
    user = request.user
    if user.is_authenticated:
        if user.is_student:
            if request.method == 'POST':
                reqs = UserRequest.objects.get(pk=pk)
                reqs.delete()
        return redirect('requests')
    else:
        return redirect('home')

def respond(request, pk):
    user = request.user
    if user.is_authenticated:
        if user.is_mentor:
            if request.method == 'POST':
                body = parse_req_body(request.body)
                req = UserRequest.objects.get(pk=pk)
                req.mentor_response = body['mentor_response']
                if request.FILES:
                    uploaded_file = request.FILES['mentor_document']
                    req.mentor_document = uploaded_file
                req.save()

            req = UserRequest.objects.get(pk=pk)
            context = { 'req': req }
            return render(request, 'request/respond.html', context=context)
        else:
            return redirect('requests')
    else:
        return redirect('home')
