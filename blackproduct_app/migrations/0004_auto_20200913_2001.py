# Generated by Django 3.1.1 on 2020-09-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackproduct_app', '0003_auto_20200913_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_sys',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]