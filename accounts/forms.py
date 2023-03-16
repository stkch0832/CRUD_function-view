from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    # password = forms.CharField(
    #     label='パスワード',
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )
    confirm_password = forms.CharField(
        label='パスワード（確認用）',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password')
        labels = {
            'email': 'メールアドレス',
            'password': 'パスワード'
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='メールアドレス',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        required=True,
        label='パスワード',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
