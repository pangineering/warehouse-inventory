# Generated by Django 4.0.4 on 2022-07-06 10:03

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('buy_sell', '0002_selling_purchase_items_alter_purchase_p_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='items',
            field=jsonfield.fields.JSONField(blank=True, default=''),
        ),
    ]