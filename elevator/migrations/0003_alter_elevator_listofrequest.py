# Generated by Django 3.2.5 on 2022-08-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator', '0002_auto_20220822_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='listofRequest',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
