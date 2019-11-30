from django.shortcuts import render

# Create your views here.
def view_student_profile(request):
    return render(request, 'student_profile/student_profile.html')




