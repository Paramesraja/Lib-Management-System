# Generated by Django 3.2.9 on 2022-01-23 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libr', '0008_auto_20220122_1518'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='order',
            name='issuedate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
