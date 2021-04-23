# Generated by Django 3.2 on 2021-04-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('item_name', models.CharField(blank=True, max_length=100, null=True)),
                ('received_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('stock_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issued_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issued_by', models.CharField(blank=True, max_length=100, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('returned_date', models.DateTimeField(auto_now=True)),
                ('stock_received_date', models.DateTimeField(auto_now=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
                ('sizes_ferrules', models.IntegerField(choices=[('one', '1'), ('one comma five', '1.5'), ('four', '4')])),
                ('condition_returned', models.TextField()),
                ('sizes_words', models.CharField(choices=[('SMALL', 'small'), ('MEDIUM', 'medium'), ('LARGE', 'large '), ('EXTRA_LARGE', 'extra-large')], max_length=100)),
            ],
        ),
    ]