from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/home.html')

"""
# Signin, Authentication
"""
def regist(request):
    regist_form = forms.UserCreationForm(request.POST or None)
    if regist_form.is_valid():
        try:
            user = regist_form.save(commit=False)
            messages.success(request, 'ユーザー登録が完了しました')
            user.save()
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


"""
# Profile
"""

@login_required
def profile_detail(request, pk):
    profile_data = Profile.objects.get(user_id=pk)
    return render(request, 'accounts/profile.html', context={
        'profile_data': profile_data,
    })


@login_required
def profile_edit(request, pk):
    profile_data = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile_form = forms.UserProfileForm(
            request.POST or None,
            request.FILES or None,
            instance=profile_data
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'プロフィールが更新されました')
            return redirect('accounts:home')
    else:
        profile_form = forms.UserProfileForm(initial= {
            'username': profile_data.username,
            'introduction': profile_data.introduction,
            'birth': profile_data.birth,
            'image': profile_data.image,
            })

    return render(request, 'accounts/form_profile.html', context={
        'profile_form': profile_form,
    })
