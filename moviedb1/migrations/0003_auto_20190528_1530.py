# Generated by Django 2.2.1 on 2019-05-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb1', '0002_auto_20190527_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('None', 'None'), ('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama')], max_length=10),
        ),
    ]