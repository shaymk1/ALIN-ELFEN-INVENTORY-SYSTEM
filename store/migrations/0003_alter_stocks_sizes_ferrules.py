# Generated by Django 3.2 on 2021-04-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_stocks_sizes_ferrules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='sizes_ferrules',
            field=models.IntegerField(choices=[(1, 'one'), (1.5, 'one point five'), (2, 'two'), (4, 'four'), (6, 'six'), (8, 'eight'), (25, 'twenty five'), (35, 'thirty five'), (50, 'fifty'), (70, 'seventy'), (95, 'ninety five'), (120, 'one hundred and twenty'), (150, 'one hundred and fifty'), (185, 'one hundred ans eighty five'), (300, 'three hundred')]),
        ),
    ]