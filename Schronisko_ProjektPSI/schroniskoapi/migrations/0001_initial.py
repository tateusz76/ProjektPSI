# Generated by Django 3.2.9 on 2021-11-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zwierze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('rasa', models.CharField(max_length=30)),
                ('rokUrodzenia', models.IntegerField()),
                ('rokPrzygarniecia', models.IntegerField()),
                ('typ', models.IntegerField()),
            ],
        ),
    ]
