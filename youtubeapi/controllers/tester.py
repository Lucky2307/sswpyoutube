from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from youtubeapi.models.channel import Channel
from youtubeapi.models.video import Video

from .youtube_xml import fetchChannelXML
from .helper import refreshFeeds, refreshWatchlist, saveNewChannel

'''
these tester is for testing only, integrate 
it properly with the template once its done
'''

# register new channel to db
# access by 'http://localhost:8000/youtubeapi/tester/channel/save/<channelId>/'
def confirmSaveChannel(request, channelId):
    numOfVids = saveNewChannel(channelId)
    if numOfVids:
        return HttpResponse('Channel saved. %d archived video(s) found.' % numOfVids)
    else:
        # implement the error msg!!!! but i dont even know what kind of error this'll produce, if any.
        return HttpResponse('something went wrong, maybe the channelId doesnt exist')


# look for new videos of all channel from the XML feed
# access by 'http://localhost:8000/youtubeapi/tester/update/feeds/'
def updateRecentFeeds(request):
    channels = Channel.objects.all()
    numOfVids = refreshFeeds()
    return HttpResponseRedirect(reverse('videos-index'))

# Update the metadata of all upcoming and live video, use this to figure out if an upcoming
# live stream has started or otherwise, ongoing live stream has ended
# access by 'http://localhost:8000/youtubeapi/tester/update/watchlist/'
def updateWatchlist(request):

    watchlistedVideoIdList = refreshWatchlist()

    return HttpResponseRedirect(reverse('videos-index'))
