from django.shortcuts import render, redirect
# using built-in django form
from .forms import RegisterForm

# Create your views here.
def register(response):
    # we have to pass the form here
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save() # this will save the user in the user database
        # return redirect("/home") -- will redirect to home page when we create it
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})



