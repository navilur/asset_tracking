# Generated by Django 4.2.1 on 2023-08-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_manager', '0002_alter_devicelog_return_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelog',
            name='return_condition',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='return_date',
            field=models.DateTimeField(),
        ),
    ]
