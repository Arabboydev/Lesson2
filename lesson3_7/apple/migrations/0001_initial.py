# Generated by Django 5.0.4 on 2024-04-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppleAirPods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IphonePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
            ],
        ),
    ]
