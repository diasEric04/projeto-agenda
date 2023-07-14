from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Usuario criado com sucesso. Efetue o login'
            )
            return redirect('contact:user/login')
        context = {
            'title': 'Register',
            'form': form
        }
        return render(
            request,
            'user/register.html',
            context
        )
    context = {
        'title': 'Register',
        'form': RegisterForm()
    }
    return render(
        request,
        'user/register.html',
        context
    )


def login_view(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'logado com sucesso')
            return redirect('contact:index')

    context = {
        'title': 'Login',
        'form': form
    }
    return render(
        request,
        'user/login.html',
        context
    )


@login_required(login_url='contact:index')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:user/login')


@login_required(login_url='contact:user/login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'user/update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'user/update.html',
            {
                'form': form
            }
        )

    form.save()
    messages.success(request, 'dados alterados com sucesso')
    return redirect('contact:user/update')
