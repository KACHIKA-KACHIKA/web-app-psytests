# Generated by Django 4.2.1 on 2023-05-22 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0008_rename_users_id_user_answers_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='userInfo',
            new_name='users_id_user',
        ),
    ]
