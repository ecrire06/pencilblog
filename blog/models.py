from django.conf import settings
from django.db import models

# ============INSTALLED APPS==============
from taggit.managers import TaggableManager
from django_editorjs_fields import EditorJsTextField, EditorJsJSONField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body_editorjs_custom = EditorJsJSONField(
        plugins=[
            "@editorjs/image",
            "@editorjs/header",
            "editorjs-github-gist-plugin",
            "@editorjs/code@2.6.0",  # version allowed :)
            "@editorjs/list@latest",
            "@editorjs/inline-code",
            "@editorjs/table",
        ],
        tools={
            "Gist": {
                "class": "Gist"  # Include the plugin class. See docs Editor.js plugins
            },
            "Image": {
                "config": {
                    "endpoints": {
                        "byFile": "/uploads"  # Your custom backend file uploader endpoint
                    }
                }
            }
        },
        i18n={
            'messages': {
                'blockTunes': {
                    "delete": {
                        "Delete": "삭제"
                    },
                    "moveUp": {
                        "Move up": "위로"
                    },
                    "moveDown": {
                        "Move down": "아래로"
                    }
                }
            },
        },
        null=True,
        blank=True
        )
#    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
