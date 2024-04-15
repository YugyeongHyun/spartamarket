from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
    else:
        form = AuthenticationForm()
        context = {"form": form}
    return render(request, 'accounts/login.html', context)
