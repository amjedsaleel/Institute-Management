# Generated by Django 3.1.4 on 2020-12-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0003_auto_20201214_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='address',
            field=models.TextField(blank=True, default='nile', help_text='Provide address of the institute', max_length=255),
        ),
        migrations.AlterField(
            model_name='institute',
            name='name',
            field=models.CharField(help_text='eg:- Kozhikode Institute', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='institute',
            name='phone_no',
            field=models.CharField(blank=True, default='nill', help_text='eg:- 0495 2211545', max_length=15),
        ),
        migrations.AlterField(
            model_name='institute',
            name='short_name',
            field=models.CharField(help_text='eg:- KI', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='institute',
            name='website',
            field=models.URLField(blank=True, default='www.example.com', help_text='eg:- kozhikodeinstitute.com'),
        ),
    ]
