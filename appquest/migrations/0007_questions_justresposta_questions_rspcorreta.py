# Generated by Django 4.2.5 on 2023-09-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquest', '0006_alter_questions_tipoquestao'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='justresposta',
            field=models.CharField(blank=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='rspcorreta',
            field=models.CharField(blank=True),
        ),
    ]
