# Generated by Django 3.1.4 on 2020-12-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('institute', 'Institute'), ('teacher', 'Teacher'), ('student', 'Student')], help_text='Chose user role', max_length=15),
        ),
    ]