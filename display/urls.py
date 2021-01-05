from django.urls import path
from .controllers import livestreams, channels

urlpatterns = [
    path('videos/feeds/', livestreams.videosIndex, name='videos-index'),
    path('videos/archive/', livestreams.archivedVideosView, name='videos-archive'),

    path('channel/all/', channels.channelsIndex, name='channel-index'),
    path('channel/<str:channelId>/', channels.channelDetail, name='channel-detail'),
    path('channel/save/<str:channelId>/', channels.confirmSaveChannel, name='confirm-save-channel'),
    path('channel/update/<str:channelId>/', channels.UpdateChannel, name='channel-update'),
    path('channel/delete/<str:channelId>/', channels.DeleteChannel, name='channel-delete'),
]