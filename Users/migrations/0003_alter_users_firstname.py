# Generated by Django 4.0.3 on 2022-04-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_payments_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
