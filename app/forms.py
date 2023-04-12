from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    post_text = forms.CharField(
        label='投稿内容',
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Post
        fields = ['post_text']
