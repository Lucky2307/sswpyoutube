from django.urls import path
from .controllers import livestreams, channels, footer

urlpatterns = [
    path('videos/feeds/', livestreams.videosIndex, name='videos-index'),
    path('videos/archive/', livestreams.archivedVideosView, name='videos-archive'),

    path('channel/all/', channels.channelsIndex, name='channel-index'),
    path('channel/<str:channelId>/', channels.channelDetail, name='channel-detail'),
    path('channel/save/<str:channelId>/', channels.confirmSaveChannel, name='confirm-save-channel'),

    path('footer/help', footer.footer, name='footer-help'),
    path('footer/about', footer.footer, name='footer-about'),
]