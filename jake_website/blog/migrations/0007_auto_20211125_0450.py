# Generated by Django 3.2.5 on 2021-11-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211125_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='../assets/None/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, default='', upload_to='../assets/None/'),
        ),
    ]