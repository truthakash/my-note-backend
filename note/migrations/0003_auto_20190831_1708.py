# Generated by Django 2.2.4 on 2019-08-31 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20190830_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
