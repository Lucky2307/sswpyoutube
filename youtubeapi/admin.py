from django.contrib import admin

from youtubeapi.models import channel, video, language, agency

# Register your models here.
admin.site.register(channel.Channel)
admin.site.register(video.Video)
admin.site.register(language.Language)
admin.site.register(agency.Agency)