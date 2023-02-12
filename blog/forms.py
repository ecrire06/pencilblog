from django import forms
from django_editorjs_fields import EditorJsWidget

from django.db import models
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['created_date']
    widgets = {
            'body_editorjs': EditorJsWidget(config={'minHeight': 100}),
    }