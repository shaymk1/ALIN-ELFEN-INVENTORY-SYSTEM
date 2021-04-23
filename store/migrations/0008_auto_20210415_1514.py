# Generated by Django 3.2 on 2021-04-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210415_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='condition_returned',
            field=models.TextField(blank=True),
        ),
    ]
