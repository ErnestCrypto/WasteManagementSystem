# Generated by Django 4.0.3 on 2022-04-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrators',
            name='username',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
