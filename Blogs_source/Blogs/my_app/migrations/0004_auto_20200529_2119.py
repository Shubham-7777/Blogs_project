# Generated by Django 3.0.2 on 2020-05-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20200528_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(max_length=150),
        ),
    ]