# Generated by Django 3.1.3 on 2023-06-11 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0009_auto_20230611_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='grade',
            new_name='mark',
        ),
    ]
