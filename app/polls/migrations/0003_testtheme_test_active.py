# Generated by Django 3.0.3 on 2021-04-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_testtheme_final_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtheme',
            name='test_active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
