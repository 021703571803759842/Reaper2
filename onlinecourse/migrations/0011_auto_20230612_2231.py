# Generated by Django 3.1.3 on 2023-06-12 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0010_auto_20230611_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='mark',
            new_name='grade',
        ),
    ]