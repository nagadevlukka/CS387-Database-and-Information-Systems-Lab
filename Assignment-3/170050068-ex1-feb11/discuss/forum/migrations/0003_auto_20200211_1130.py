# Generated by Django 3.0.2 on 2020-02-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200211_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
