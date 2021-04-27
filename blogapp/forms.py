from django import forms
from django.contrib.auth.models import User
from .models import Comment
from django.contrib.auth.forms import UserCreationForm


class UserCommentForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    date_created = forms.DateTimeField()
    comment = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['username', 'email', 'date_created', 'comment']

