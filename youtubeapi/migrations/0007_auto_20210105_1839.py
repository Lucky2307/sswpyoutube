# Generated by Django 3.1.4 on 2021-01-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapi', '0006_auto_20210105_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='icon',
            field=models.ImageField(null=True, upload_to='agencies/'),
        ),
        migrations.AlterField(
            model_name='language',
            name='icon',
            field=models.ImageField(null=True, upload_to='flags_icon/'),
        ),
    ]
