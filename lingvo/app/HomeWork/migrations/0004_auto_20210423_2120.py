# Generated by Django 3.1.7 on 2021-04-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeWork', '0003_auto_20210423_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]