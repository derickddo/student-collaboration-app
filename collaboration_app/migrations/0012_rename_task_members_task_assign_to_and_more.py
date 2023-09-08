# Generated by Django 4.2.1 on 2023-06-09 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration_app', '0011_task_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_members',
            new_name='assign_to',
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='collaboration_app.group'),
        ),
    ]
