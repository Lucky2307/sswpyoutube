from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages

from datetime import datetime, timedelta

from youtubeapi.models.video import Video

def videosIndex(request):
    upcomingVideos = Video.objects.filter(liveBroadcastContent='upcoming', scheduledStartTime__gte=datetime.now() ,scheduledStartTime__lte=datetime.now()+timedelta(days=3)).order_by('scheduledStartTime')
    liveVideos = Video.objects.filter(liveBroadcastContent='live').order_by('actualStartTime')
    recentlyEndedStreams = Video.objects.filter(liveBroadcastContent='none', publishedAt__gte=datetime.now()-timedelta(hours=12)).order_by('-actualStartTime')

    data = {
        'upcomingVideos':upcomingVideos,
        'liveVideos':liveVideos,
        'recentlyEndedStreams':recentlyEndedStreams,
    }

    return render(request, 'stream/index.html', context=data)