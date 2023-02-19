from django.conf import settings
from django.db import models
from django.urls import reverse_lazy

# ============INSTALLED APPS==============
from taggit.managers import TaggableManager
from django_editorjs_fields import EditorJsTextField, EditorJsJSONField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body_editorjs_custom = EditorJsTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
