# Generated by Django 3.2.13 on 2023-02-12 05:08

from django.db import migrations
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_body_editorjs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_editorjs',
        ),
        migrations.AddField(
            model_name='post',
            name='body_editorjs_custom',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
    ]