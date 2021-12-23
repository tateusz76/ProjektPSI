# Generated by Django 3.2.9 on 2021-12-17 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchroniskoAPI', '0019_zabieg_datazabiegu'),
    ]

    operations = [
        migrations.AddField(
            model_name='zabieg',
            name='rodzajZabiegu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rodzaje', to='SchroniskoAPI.rodzajezabiegow'),
            preserve_default=False,
        ),
    ]
