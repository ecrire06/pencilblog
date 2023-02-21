from django.conf import settings
from django.db import models
from django.urls import reverse_lazy

# ============INSTALLED APPS==============
from taggit.managers import TaggableManager
from django_editorjs_fields import EditorJsTextField, EditorJsJSONField
from cloudinary.models import CloudinaryField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body_editorjs_custom = EditorJsTextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    tags = TaggableManager()
    image = CloudinaryField(blank=True, null=True)
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment[:60]