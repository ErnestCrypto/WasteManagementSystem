# Generated by Django 4.0.3 on 2022-05-10 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]