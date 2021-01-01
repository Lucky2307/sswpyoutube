# Generated by Django 3.1.4 on 2020-12-29 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channelId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100, null=True)),
                ('uploadPlaylist', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('videoId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=100)),
                ('publishedAt', models.DateTimeField(null=True)),
                ('liveBroadcastContent', models.CharField(choices=[('live', 'Live'), ('none', 'Archived'), ('upcoming', 'Upcoming')], default='none', max_length=10)),
                ('scheduledStartTime', models.DateTimeField(null=True)),
                ('actualStartTime', models.DateTimeField(null=True)),
                ('actualEndTime', models.DateTimeField(null=True)),
                ('channelId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeapi.channel')),
            ],
        ),
    ]