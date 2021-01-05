from django.db import models
from youtubeapi.models.language import Language
from youtubeapi.models.agency import Agency

# represents a YouTube channel
class Channel(models.Model):
    channelId = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True) # nullable, new channel might not have thumbnail in youtube api
    uploadPlaylist = models.CharField(max_length=100, null=True) # nullable, new channel might not have a video
    language = models.ManyToManyField(Language)
    agency = models.ForeignKey(Agency, null=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'youtubeapi'
        
    def __str__(self):
        return f'{self.name}'