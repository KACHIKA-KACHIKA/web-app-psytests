# Generated by Django 4.2.1 on 2023-05-22 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0010_answers_userinfo_alter_answers_users_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='users_id_user',
        ),
    ]
