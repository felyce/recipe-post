# Generated by Django 3.1.6 on 2021-02-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20210211_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/uploaded/'),
        ),
    ]