# Generated by Django 2.0.7 on 2019-09-17 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='email',
            new_name='order_id',
        ),
    ]
