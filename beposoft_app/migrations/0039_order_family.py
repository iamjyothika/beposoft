# Generated by Django 5.1 on 2024-10-26 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beposoft_app', '0038_order_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='family',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beposoft_app.family'),
            preserve_default=False,
        ),
    ]
