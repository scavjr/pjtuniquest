# Generated by Django 4.2.5 on 2023-09-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquest', '0002_alter_questions_qimagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altquestion',
            name='altjustif',
            field=models.TextField(blank=True),
        ),
    ]
