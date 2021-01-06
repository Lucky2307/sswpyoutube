from django.shortcuts import render
from django.core.paginator import Paginator

from datetime import datetime, timedelta

from youtubeapi.models.video import Video
from display.filters import OrderVideo

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
    videos_list = Video.objects.filter(liveBroadcastContent='none').order_by('-publishedAt')

    myFilter = OrderVideo(request.GET, queryset=videos_list)
    videos_list = myFilter.qs

    paginator = Paginator(videos_list, 15)

    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.page_number)
    data = {
        'page_obj':page_obj,
        'paginator':paginator,
        'myFilter': myFilter,
    }

    return render(request, 'stream/archive.html', context=data)