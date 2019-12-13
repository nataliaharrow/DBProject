from django.shortcuts import render
from helper import parse_req_body
from app_user.models import *

# Create your views here.
def view_user_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    user = request.user
    profile = Profile.objects.get(user=user)
    context = { 'profile': profile }
    return render(request, 'profile/profile.html', context=context)




