# Generated by Django 3.1.2 on 2020-10-19 12:29

from django.db import migrations, models
import insta.models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20201019_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to=insta.models.get_image_path),
        ),
    ]