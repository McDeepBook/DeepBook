# Generated by Django 2.1.3 on 2018-11-28 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xray', '0003_auto_20181128_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xray',
            name='user',
        ),
    ]
