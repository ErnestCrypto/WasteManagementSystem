# Generated by Django 4.0.3 on 2022-04-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_alter_payments_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='day',
            field=models.IntegerField(choices=[(1, 'MONDAY'), (2, 'TUESDAY'), (3, 'WEDNESDAY'), (4, 'THURSDAY'), (5, 'FRIDAY'), (6, 'SATURDAY'), (7, 'SUNDAY')], default=None),
        ),
    ]
