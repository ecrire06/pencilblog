# Generated by Django 3.2.13 on 2023-02-12 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_body_editorjs_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_editorjs_text',
        ),
    ]