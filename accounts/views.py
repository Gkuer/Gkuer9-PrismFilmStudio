from django.shortcuts import render,redirect
from .forms import CustomUserCreationFrom
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index', 1)
    
    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationFrom()
    context = {
        'form': form
    }
    return render(request,'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index', 1)
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:choice')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html', context)


@require_http_methods(['GET','POST'])
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')