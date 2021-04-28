# Generated by Django 3.2 on 2021-04-24 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date_issued',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date_returned',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
