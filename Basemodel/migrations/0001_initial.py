# Generated by Django 4.0.3 on 2022-05-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelpCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None, null=True)),
                ('message', models.TextField(default=None)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pricings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('type', models.IntegerField(choices=[(1, 'one time payment'), (2, 'subscription')], default=None)),
            ],
            options={
                'verbose_name_plural': 'Pricings',
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved')], default=None)),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
        ),
    ]
