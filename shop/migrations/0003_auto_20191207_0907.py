# Generated by Django 2.2.7 on 2019-12-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191207_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.FileField(blank=True, upload_to='profille_picture'),
        ),
        migrations.AlterField(
            model_name='member',
            name='post_code',
            field=models.CharField(max_length=10),
        ),
    ]
