# Generated by Django 3.2 on 2021-04-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210416_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='sizes_ferrules',
            field=models.CharField(choices=[('N/A', 'n/a'), ('zero', 'zero'), ('one', 1), ('one comma five', 1.5), ('two', 2), ('four', 4), ('six', 6), ('eight', 8), ('twenty five', 25), ('thirty five', 35), ('fifty', 50), ('seventy', 70), ('ninety five', 95), ('one hundred and twenty', 120), ('one hundred and fifty', 150), ('one hundred ans eighty five', 185), ('three hundred', 300)], max_length=100),
        ),
    ]
