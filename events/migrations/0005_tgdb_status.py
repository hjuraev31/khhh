# Generated by Django 4.0.4 on 2022-07-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_tgdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgdb',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
