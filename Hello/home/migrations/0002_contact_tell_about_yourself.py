# Generated by Django 4.2.7 on 2023-11-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='tell_about_yourself',
            field=models.TextField(blank=True),
        ),
    ]
