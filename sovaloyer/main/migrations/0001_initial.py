# Generated by Django 4.2.1 on 2024-01-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.IntegerField()),
                ('time_game', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
