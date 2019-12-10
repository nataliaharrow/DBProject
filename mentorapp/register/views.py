from django.shortcuts import render, redirect
from .forms import StudentRegisterForm, MentorRegisterForm
from app_user.models import User, UserProfile, School, Major, Company, Industry, Request #, UserSchool, UserMajor, UserCompany, UserIndustry, UserRequest, Connection, CompanyIndustry


def register(request):
    return render(request, "register/register.html")


def student_register(request):
    if request.method == "POST":
        student_form = StudentRegisterForm(request.POST)
        if student_form.is_valid():
            user = student_form.save(commit=False)
            user.is_student = True
            # school = School.objects.all()[int(student_form.cleaned_data["school"]) - 1]
            major_save = Major.objects.all()[int(student_form.cleaned_data["major"]) - 1]
            industry = Industry.objects.all()[int(student_form.cleaned_data["industry"]) - 1]
            requests = student_form.cleaned_data["requests"]
            user.save()
            user.majors.add(major_save)
            user.industries.add(industry)
            for new_request in requests:
                user.requests.add(new_request)
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()
    else:
        student_form = StudentRegisterForm()
    return render(request, "register/student_register.html", {"student_form": student_form})


def mentor_register(request):
    if request.method == "POST":
        mentor_form = MentorRegisterForm(request.POST)
        if mentor_form.is_valid():
            user = mentor_form.save(commit=False)
            user.is_mentor = True
            major_save = Major.objects.all()[int(mentor_form.cleaned_data["major"]) - 1]
            industry = Industry.objects.all()[int(mentor_form.cleaned_data["industry"]) - 1]
            requests = mentor_form.cleaned_data["requests"]
            company = mentor_form.cleaned_data["company"]
            user.save()
            user.majors.add(major_save)
            user.industries.add(industry)
            user.companies.add(company)
            for new_request in requests:
                user.requests.add(new_request)
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()
    else:
        mentor_form = MentorRegisterForm()
    return render(request, "register/mentor_register.html", {"mentor_form": mentor_form})


# from django.shortcuts import render, redirect
# from .forms import RegisterForm, StudentMentorForm
#
#
# def student_register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         student_mentor_form = StudentMentorForm(request.POST)
#         if form.is_valid() and student_mentor_form.is_valid():
#             user = form.save()
#
#             # app_user = user_app_form.save(commit=False)
#             # app_user.user = user
#             # app_user.is_student = user_app_form.cleaned_data["student"]
#             # app_user.is_mentor = user_app_form.cleaned_data["mentor"]
#             # app_user.save()
#
#             if student_mentor_form.cleaned_data["student"] == True:
#                 student = student_form.save(commit=False)
#                 student.user = user
#                 student.save()
#
#             if mentor_form.cleaned_data["mentor"] == True:
#                 mentor = mentor_form.save(commit=False)
#                 mentor.user = user
#                 mentor.save()
#             # username = form.cleaned_data["username"]
#             # first_name = form.cleaned_data["first_name"]
#             # last_name = form.cleaned_data["last_name"]
#             # email = form.cleaned_data["email"]
#             #
#             # student = user_app_form.cleaned_data["student"]
#             # mentor = user_app_form.cleaned_data["mentor"]
#
#             # newUser = User.objects.create(username= form_username, first_name=form_first_name, last_name=form_last_name, email_address=form_email, is_student=form_student, is_mentor=form_mentor)
#             # newUser.save()
#             # form.save() # this will save the app_user in the app_user database
#         # return redirect("/home") -- will redirect to home page when we create it
#     else:
#         form = RegisterForm()
#         student_form = StudentForm()
#         mentor_form = MentorForm()
#     return render(request, "register/register.html", {"form":form, "student_form": student_form, "mentor_form": mentor_form})
