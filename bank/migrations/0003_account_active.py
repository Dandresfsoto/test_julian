# Generated by Django 3.1.2 on 2020-10-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
