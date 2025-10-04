from django import forms

from .models import Comment


class AuthenticatedCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'stars', 'recommendation', ]


class AnonymousCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'author_email', 'text', 'stars', 'recommendation', ]
