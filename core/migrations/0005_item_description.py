# Generated by Django 2.1.5 on 2020-07-22 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Test description'),
            preserve_default=False,
        ),
    ]