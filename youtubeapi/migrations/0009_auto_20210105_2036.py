# Generated by Django 3.1.4 on 2021-01-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapi', '0008_auto_20210105_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='language',
            field=models.ManyToManyField(blank=True, null=True, to='youtubeapi.Language'),
        ),
    ]