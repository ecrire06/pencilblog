# Generated by Django 3.2.13 on 2023-03-16 11:12

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_post_body_froala'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_quill',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
