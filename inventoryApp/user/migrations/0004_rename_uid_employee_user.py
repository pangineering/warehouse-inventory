# Generated by Django 4.0.4 on 2022-05-08 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='uid',
            new_name='user',
        ),
    ]
