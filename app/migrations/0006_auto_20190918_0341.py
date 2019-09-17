# Generated by Django 2.0.7 on 2019-09-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190918_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='admin_id',
            field=models.CharField(default='2121', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='delivered_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='est_delivery_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='is_upload',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='photo_url',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='orders',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.CharField(default='233422', max_length=15),
            preserve_default=False,
        ),
    ]
