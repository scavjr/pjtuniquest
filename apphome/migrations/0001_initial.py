# Generated by Django 4.2.5 on 2023-09-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListQuestAtual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField()),
            ],
        ),
    ]
