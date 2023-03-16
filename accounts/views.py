from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/home.html')


def regist(request):
    regist_form = forms.UserCreationForm(request.POST or None)
    if regist_form.is_valid():
        try:
            regist_form.save()
            messages.success(request, 'ユーザー登録が完了しました')
            return redirect('accounts:home')
        except ValidationError as e:
            regist_form.add_error('password', e)
    return render(
        request, 'accounts/regist.html', context={
            'regist_form': regist_form,
        }
    )


def user_login(request):
    login_form = forms.UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'ログインが完了しました')
                return redirect('accounts:home')
            else:
                messages.warning(request, '有効なアカウントではありません')
        else:
            messages.warning(request, 'メールアドレスまたはパスワードが間違っています')
    return render(request, 'accounts/login.html', context={
        'login_form': login_form,
    })


@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, 'ログアウトしました')
    return redirect('accounts:home')
