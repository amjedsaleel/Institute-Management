# Generated by Django 3.1.4 on 2020-12-13 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201213_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='updatedon',
            new_name='update_don',
        ),
    ]