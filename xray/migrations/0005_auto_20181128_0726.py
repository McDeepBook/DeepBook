# Generated by Django 2.1.3 on 2018-11-28 07:26

from django.db import migrations
import imagekit.models.fields
import xray.models


class Migration(migrations.Migration):

    dependencies = [
        ('xray', '0004_remove_xray_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xray',
            options={},
        ),
        migrations.RemoveField(
            model_name='xray',
            name='result',
        ),
        migrations.RemoveField(
            model_name='xray',
            name='time',
        ),
        migrations.AlterField(
            model_name='xray',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=xray.models.post_image_path),
        ),
    ]
