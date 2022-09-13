from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    # POST
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():

            # UserCreationForm saves username and password to db
            user = form.save()

            # Login
            login(request, user)

            # Redirect somewhere
            return redirect("home")
    # GET
    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }

    return render(request, "registration/signup.html", context)
