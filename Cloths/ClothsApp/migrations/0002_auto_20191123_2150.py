# Generated by Django 2.2.4 on 2019-11-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClothsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='days_for_clearing',
            field=models.IntegerField(default=None),
        ),
    ]
