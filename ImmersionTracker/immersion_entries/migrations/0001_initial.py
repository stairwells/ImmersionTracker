# Generated by Django 5.0.3 on 2024-03-22 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('languages', '0001_initial'),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_length', models.DurationField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='languages.language')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='media.listeningmedia')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='accounts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReadingEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_length', models.DurationField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('char_length', models.IntegerField(default=None)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='languages.language')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='media.readingmedia')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='accounts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SRSEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_length', models.DurationField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('new_cards', models.IntegerField(blank=True, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='languages.language')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='accounts.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
