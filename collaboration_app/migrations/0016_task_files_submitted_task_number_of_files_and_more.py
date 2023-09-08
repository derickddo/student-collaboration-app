# Generated by Django 4.2.1 on 2023-07-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration_app', '0015_group_group_type_alter_messagereply_group_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='files_submitted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='number_of_files',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_file',
            field=models.FileField(upload_to='files'),
        ),
    ]