# Generated by Django 4.0.4 on 2022-07-06 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p_num', models.CharField(max_length=200)),
                ('employee_number', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('team', models.CharField(choices=[('Robotics', 'Robotics'), ('Automobile', 'Automobile'), ('Machine', 'Machine')], max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approve', 'Approve'), ('Complete', 'Complete'), ('Cancel', 'Cancel'), ('Revision', 'Revision')], max_length=200)),
                ('category', models.CharField(choices=[('Manager', 'Manager'), ('Sales', 'Sales'), ('Engineer', 'Engineer'), ('Warehouse', 'Warehouse')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
