# Generated by Django 2.2.6 on 2019-10-29 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191029_1257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Product',
        ),
    ]
