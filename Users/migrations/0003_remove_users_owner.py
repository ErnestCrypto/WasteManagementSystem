# Generated by Django 4.0.3 on 2022-05-08 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_remove_users_highlighted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='owner',
        ),
    ]
