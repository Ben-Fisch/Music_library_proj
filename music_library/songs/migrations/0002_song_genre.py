# Generated by Django 3.2.8 on 2021-10-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='r&b', max_length=50),
        ),
    ]
