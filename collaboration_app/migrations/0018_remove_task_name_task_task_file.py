# Generated by Django 4.2.1 on 2023-07-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration_app', '0017_remove_task_task_file_task_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='task_file',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]
