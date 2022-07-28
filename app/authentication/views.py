from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from .decorators import unauthenticated_user
from .forms import CreateUserForm
from .models import Profile


@login_required(login_url='auth:login')
def profile_page(request, pk):  # Показать детали профиля
    profile = Profile.objects.get(pk=pk)
    return render(request, 'authentication/profile.html', context={
        'profile': Profile.objects.get(pk=pk),
    })


@unauthenticated_user
def registration_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('auth:login')
        else:
            messages.error(request, 'Got a registration error: ' + str(form.error_messages))
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'authentication/registration.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shortener:index')
        else:
            messages.warning(request, 'Username or Password is incorrect')
    return render(request, 'authentication/login.html')


def logout_page(request):
    logout(request)
    return redirect('auth:login')
