# Generated by Django 3.2.9 on 2022-01-27 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchroniskoAPI', '0028_alter_adopcja_dataadopcji'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zwierze',
            old_name='data_adopcji',
            new_name='id_adopcji',
        ),
    ]
