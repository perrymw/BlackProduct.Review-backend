# Generated by Django 3.1 on 2020-08-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackproduct_app', '0002_auto_20200824_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rewiew',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(max_length=1001, upload_to='media'),
        ),
    ]