# Generated by Django 4.0.3 on 2022-04-05 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_delete_helpcenter_delete_pricings_delete_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='profile',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]