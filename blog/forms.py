from django import forms
from django.db import models
from django_editorjs_fields import EditorJsWidget
from django.core.exceptions import ValidationError
from .models import Post, Comment

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['created_date', 'is_published', 'author']
    widgets = {
            'body_editorjs': EditorJsWidget(config={'minHeight': 100}),
    }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
      
    def __init__(self, *args, **kwargs):
        """Save the request with the form so it can be accessed in clean_*()"""
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        """Make sure people don't use my name"""
        data = self.cleaned_data['name']
        if not self.request.user.is_authenticated and data.lower().strip() == 'ecrire06':
            raise ValidationError("Sorry, you cannot use this name.")
        return data