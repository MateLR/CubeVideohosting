# Generated by Django 4.1.5 on 2023-06-09 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cubeapp', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_at',
        ),
    ]