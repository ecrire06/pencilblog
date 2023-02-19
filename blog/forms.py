from django import forms
from django.db import models
from django_editorjs_fields import EditorJsWidget
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['created_date', 'published_date', 'author']
    widgets = {
            'body_editorjs': EditorJsWidget(config={'minHeight': 100}),
    }

# CHECK https://stackoverflow.com/questions/70354455/django-not-showing-images-in-editor-404-error