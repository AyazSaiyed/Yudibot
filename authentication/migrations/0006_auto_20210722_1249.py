# Generated by Django 3.0.5 on 2021-07-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210625_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usersname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]