# Generated by Django 3.1.4 on 2021-01-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapi', '0003_auto_20210105_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]