# Generated by Django 5.0.3 on 2024-03-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningmedia',
            name='status',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Completed', 'Completed'), ('On Hold', 'On Hold'), ('Dropped', 'Dropped')], max_length=10),
        ),
    ]
