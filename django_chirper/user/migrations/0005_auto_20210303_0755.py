# Generated by Django 3.1.5 on 2021-03-03 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210303_0751'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follower',
            new_name='Following',
        ),
    ]
