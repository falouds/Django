# Generated by Django 2.0 on 2020-03-28 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0005_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='kddcup',
        ),
        migrations.DeleteModel(
            name='kddcuptest',
        ),
    ]
