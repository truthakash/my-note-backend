# Generated by Django 2.2.4 on 2019-09-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20190901_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(max_length=145),
        ),
    ]
