# Generated by Django 5.1.2 on 2024-12-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tumbler', '0004_remove_tumbler_is_promo_tumbler_is_recommended'),
    ]

    operations = [
        migrations.AddField(
            model_name='tumbler',
            name='is_promo',
            field=models.BooleanField(default=False),
        ),
    ]
