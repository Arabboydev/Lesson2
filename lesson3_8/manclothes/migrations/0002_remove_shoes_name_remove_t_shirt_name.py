# Generated by Django 5.0.4 on 2024-04-30 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manclothes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoes',
            name='name',
        ),
        migrations.RemoveField(
            model_name='t_shirt',
            name='name',
        ),
    ]
