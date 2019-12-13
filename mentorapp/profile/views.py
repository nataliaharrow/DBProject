from django.shortcuts import render


# Create your views here.
def view_user_profile(request):
    return render(request, 'profile/profile.html')




