# Generated by Django 2.2 on 2019-05-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_auto_20190510_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
