# Generated by Django 3.2.9 on 2021-12-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchroniskoAPI', '0002_adopcja'),
    ]

    operations = [
        migrations.AddField(
            model_name='zwierze',
            name='idAdopcja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SchroniskoAPI.adopcja'),
        ),
    ]