# Generated by Django 3.1.3 on 2023-06-11 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0007_auto_20230611_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='grade',
            new_name='question_grade',
        ),
    ]