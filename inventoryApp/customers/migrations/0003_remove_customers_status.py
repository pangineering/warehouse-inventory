# Generated by Django 4.0.4 on 2022-07-07 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customers_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='status',
        ),
    ]