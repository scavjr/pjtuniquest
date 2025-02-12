# Generated by Django 4.2.5 on 2023-09-26 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appquest', '0007_questions_justresposta_questions_rspcorreta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='rspcorreta',
        ),
        migrations.AddField(
            model_name='questions',
            name='rspcorretaid',
            field=models.ForeignKey(default=120, on_delete=django.db.models.deletion.CASCADE, to='appquest.altquestion', verbose_name='AltQuestion'),
            preserve_default=False,
        ),
    ]
