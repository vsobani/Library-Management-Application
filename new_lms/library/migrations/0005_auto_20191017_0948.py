# Generated by Django 2.2.6 on 2019-10-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_record_pay_fine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='pay_fine',
            field=models.IntegerField(default=0),
        ),
    ]
