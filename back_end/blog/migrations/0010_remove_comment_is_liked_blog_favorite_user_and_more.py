# Generated by Django 4.1 on 2024-03-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='is_liked',
        ),
        migrations.AddField(
            model_name='blog',
            name='favorite_user',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes_user',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
