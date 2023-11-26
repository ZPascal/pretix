# Generated by Django 4.2.4 on 2023-10-30 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pretixbase", "0248_item_free_price_suggestion"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="hidden_if_item_available",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pretixbase.item",
            ),
        ),
    ]