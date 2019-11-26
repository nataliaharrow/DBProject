from django.shortcuts import render, redirect
# using built-in django form
from .forms import RegisterForm
from user.models import User

# Create your views here.
def register(response):
    # we have to pass the form here
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form_username = form.cleaned_data["username"]
            form_first_name = form.cleaned_data["first_name"]
            form_last_name = form.cleaned_data["last_name"]
            form_email = form.cleaned_data["email"]
            form_student = form.cleaned_data["student"]
            form_mentor = form.cleaned_data["mentor"]
            newUser = User.objects.create(username= form_username, first_name=form_first_name, last_name=form_last_name, email_address=form_email, is_student=form_student, is_mentor=form_mentor)
            newUser.save()
            form.save() # this will save the user in the user database
        # return redirect("/home") -- will redirect to home page when we create it
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})


