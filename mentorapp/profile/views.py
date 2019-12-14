from django.shortcuts import render
from helper import parse_req_body
from app_user.models import *

# Create your views here.

def profile(request, pk):
    if request.method == 'POST':
        body = parse_req_body(request.body)
        pk = int(body['user_id'])
        if body['action'] == "Connect":
            profile_user = User.objects.get(pk=pk)
            if request.user.is_student and profile_user.is_mentor:
                Connection.objects.create(student=request.user, mentor=profile_user, request_from="S",status="P")
            elif request.user.is_mentor and profile_user.is_student:
                Connection.objects.create(student=profile_user, mentor=request.user, request_from="M",status="P")

    profile_user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=profile_user)
    
    if profile_user.is_student and request.user.is_mentor:
        profile_connection = Connection.objects.filter(student=profile_user).filter(mentor=request.user)
    elif profile_user.is_mentor and request.user.is_student:
        profile_connection = Connection.objects.filter(mentor=profile_user).filter(student=request.user)       
    else:
        profile_connection = None
        
    context = { 
        'profile': profile,
        'profile_user': profile_user,
        'profile_connection':profile_connection,
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

