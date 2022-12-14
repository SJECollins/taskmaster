from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('tasks:index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return HttpResponse(status=204)
    else:
        form = AccountAuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return HttpResponse(status=204)

    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('tasks:index')
