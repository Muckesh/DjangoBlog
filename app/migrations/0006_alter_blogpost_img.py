# Generated by Django 3.2.9 on 2021-11-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blogpost_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
