# Generated by Django 4.2.5 on 2023-09-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appquest', '0005_questions_tipoquestao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='tipoquestao',
            field=models.IntegerField(choices=[(1, 'AVA'), (2, 'Texto Base'), (3, 'Videoaulas'), (4, 'Slides'), (5, 'Outras')]),
        ),
    ]
