from django.shortcuts import render
from helper import parse_req_body
from app_user.models import *

# Create your views here.

def profile(request, pk):
    # if pk != request.user.pk:
    #     if request.method == 'POST':
    #         body = parse_req_body(request)
    #         if body['action'] == edit_profile:
    print(pk)
    print(request.user.pk)
    print(request)
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    context = { 
        'profile': profile,
        'pk': pk
    }
    return render(request, 'profile/profile.html', context=context)        

def edit(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = { 
        'profile': profile,
    }
    return render(request, 'profile/edit.html', context=context)        

