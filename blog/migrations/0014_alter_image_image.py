# Generated by Django 3.2.5 on 2021-12-13 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20211130_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, default='', upload_to='images/'),
        ),
    ]
