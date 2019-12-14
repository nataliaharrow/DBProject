from django.shortcuts import render
from helper import parse_req_body
from app_user.models import *

# Create your views here.

def profile(request, pk):
    profile_user = User.objects.get(pk=pk)
    
    if pk != request.user.pk:
        if request.method == 'POST':
            body = parse_req_body(request)
            if body['action'] == "Connect":
                if request.user.is_student:
                    Connection.objects.create(student=request.user, mentor=profile_user, request_from="S",status="P")
                elif request.user.is_mentor:
                    Connection.objects.create(student=profile_user, mentor=request.user, request_from="M",status="P")
    
    
    profile = Profile.objects.get(user=profile_user)
    context = { 
        'profile': profile,
        'profile_user':profile_user,
        'pk': pk,
    }
    return render(request, 'profile/profile.html', context=context)        

def edit(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = { 
        'profile': profile,
    }
    return render(request, 'profile/edit.html', context=context)        

