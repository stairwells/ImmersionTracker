# Generated by Django 5.0.3 on 2024-03-17 07:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_alter_immersiontrackeruser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='listening_time',
            field=models.DurationField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reading_time',
            field=models.DurationField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='srs_time',
            field=models.DurationField(default='00:00:00'),
        ),
    ]
