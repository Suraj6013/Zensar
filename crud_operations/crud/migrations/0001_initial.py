# Generated by Django 5.1.5 on 2025-01-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=100)),
                ('toppings', models.CharField(max_length=100)),
            ],
        ),
    ]