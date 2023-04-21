from django import forms
from .models import Post, Comment_post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'select2_content', 'image_1', 'image_2',)

class Comment_postForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글 입력',
        widget=forms.TextInput(
            attrs={
                'placeholder': '댓글 입력칸',
                'class': 'form-control'
            }
        ),
    )

    class Meta:
        model = Comment_post
        fields = ('content',)
