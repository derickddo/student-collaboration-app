# Generated by Django 4.2.1 on 2023-05-30 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaboration_app', '0006_alter_group_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
