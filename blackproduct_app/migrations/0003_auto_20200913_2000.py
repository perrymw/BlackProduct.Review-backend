# Generated by Django 3.1.1 on 2020-09-13 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blackproduct_app', '0002_auto_20200907_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='blackproduct_app.reviews'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_sys', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blackproduct_app.product')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.ManyToManyField(through='blackproduct_app.Rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
