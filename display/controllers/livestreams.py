from django.shortcuts import render
from django.core.paginator import Paginator

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

def archivedVideosView(request):
    archivedVideos = Video.objects.filter(liveBroadcastContent='none').order_by('-publishedAt')
    paginator = Paginator(archivedVideos, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj':page_obj,
    }

    return render(request, 'stream/archive.html', context=data)