# Generated by Django 3.1.4 on 2020-12-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
    ]
