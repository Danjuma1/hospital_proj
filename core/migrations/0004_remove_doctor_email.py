# Generated by Django 3.2.8 on 2021-10-11 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_patient_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
    ]
