# Generated by Django 2.2 on 2020-06-29 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
    ]
