from django.shortcuts import render, redirect
from contact.forms import RegisterForm 
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):

    if request.user.is_authenticated:
        return redirect('contact:index')
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('contact:login')
    
    context = {
        'form': form,
    }
    return render(request, 'contact/register.html', context)

def login(request):

    if request.user.is_authenticated:
        return redirect('contact:index')
    
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Usuário logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Usuário ou senha inválidos!')
    
    context = {
        'form': form,
    }

    return render(request, 'contact/login.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário deslogado com sucesso!')
    return redirect('contact:login')