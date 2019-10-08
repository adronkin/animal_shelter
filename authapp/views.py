from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('main:index'))
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form": form})
