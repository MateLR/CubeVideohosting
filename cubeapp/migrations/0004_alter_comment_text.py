# Generated by Django 4.1.5 on 2023-06-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubeapp', '0003_remove_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
    ]
