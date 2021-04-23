# Generated by Django 3.1.7 on 2021-04-22 09:31

import HomeWork.validators
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(choices=[('B', 'Business'), ('M', 'Medicine'), ('I', 'IT')], default='B', max_length=2)),
                ('title', models.CharField(max_length=4096)),
                ('work_text', models.TextField(verbose_name='Work_text')),
                ('home_work_file', models.FileField(upload_to='Home-work/')),
                ('comment', models.TextField(verbose_name='Comments')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date_published')),
                ('finished_date', models.DateTimeField(verbose_name='Finished_date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FinishedHomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(choices=[('B', 'Business'), ('M', 'Medicine'), ('I', 'IT')], default='B', max_length=2)),
                ('title', models.CharField(default=None, max_length=4096)),
                ('finished_home_work_file', models.FileField(upload_to='Finished-home-work/', validators=[HomeWork.validators.validate_file_size, django.core.validators.FileExtensionValidator(['txt'])])),
                ('created', models.DateTimeField(auto_now=True)),
                ('mark', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Mark')),
                ('comment_of_mark', models.TextField(blank=True, null=True, verbose_name='comment_of_mark')),
                ('home_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeWork.homework', verbose_name='Home_work')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
