# Generated by Django 3.2 on 2021-04-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_stock_new_stock_received_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]