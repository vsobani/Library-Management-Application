# Generated by Django 2.2.6 on 2019-10-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='library_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
