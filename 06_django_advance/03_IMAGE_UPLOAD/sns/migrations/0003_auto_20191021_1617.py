# Generated by Django 2.2.6 on 2019-10-21 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0002_posting_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='likes',
            new_name='like_users',
        ),
    ]
