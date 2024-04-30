# Generated by Django 5.0.4 on 2024-04-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='T_Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
            ],
        ),
    ]
