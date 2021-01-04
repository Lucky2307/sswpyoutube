import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sswpyoutube.settings')
django.setup()

from youtubeapi.controllers.helper import saveNewChannel

def get_url_list(filename):
    with open(filename) as file:
        urls = [line.rstrip('\n') for line in file]
        return urls

def get_channelId_list(url_list):
    channelId_list = [ url[32:] for url in url_list ]
    return channelId_list

if __name__ == "__main__":
    t1 = time.time()
    # This will run synchronously, depending on how many videos there are in a channel,
    # this might take a while. But you only have to do this once.
    urls_list = get_url_list('channel_urls.txt')
    channelId_list = get_channelId_list(urls_list)
    numOfVids = 0
    for channelId in channelId_list:
        numOfVids += saveNewChannel(channelId)
    t2 = time.time()
    print('saved %s channels, %s videos, took %s seconds' % (len(channelId_list), numOfVids, t2 - t1))