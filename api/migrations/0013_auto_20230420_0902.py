# Generated by Django 3.2.16 on 2023-04-20 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20230420_0410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='user',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='user',
            new_name='teacher',
        ),
    ]
