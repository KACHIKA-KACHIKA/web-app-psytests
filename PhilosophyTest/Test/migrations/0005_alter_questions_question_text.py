# Generated by Django 4.2.1 on 2023-05-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0004_alter_questions_id_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=models.CharField(max_length=255),
        ),
    ]
