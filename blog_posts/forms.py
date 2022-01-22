from django import forms
from django.db.models import fields
from .models import Comment, Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'content']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ['content']