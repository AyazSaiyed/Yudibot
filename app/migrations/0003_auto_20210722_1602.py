# Generated by Django 3.0.5 on 2021-07-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobapplicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientenquiries',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clientenquiries',
            name='deactivated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clientenquiries',
            name='onhold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobapplicants',
            name='pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobapplicants',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jobapplicants',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]