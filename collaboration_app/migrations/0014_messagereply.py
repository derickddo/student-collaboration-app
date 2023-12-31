# Generated by Django 4.2.1 on 2023-07-12 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration_app', '0013_groupmessage_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collaboration_app.groupmessage')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'message_reply',
            },
        ),
    ]
