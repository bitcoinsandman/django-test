# Generated by Django 2.1.1 on 2018-09-20 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectives',
            name='objectiveDescription',
            field=models.TextField(default='undefined'),
        ),
        migrations.AddField(
            model_name='objectives',
            name='objectiveScore',
            field=models.PositiveSmallIntegerField(default='0'),
        ),
    ]
