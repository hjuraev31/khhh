# Generated by Django 4.0.4 on 2022-07-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_imgdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='TgDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('chat_id', models.TextField(default='')),
            ],
        ),
    ]
