from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
login_required = login_required(login_url='user:login')

from youtubeapi.models.channel import Channel
from youtubeapi.models.video import Video
from youtubeapi.controllers.helper import isChannelExist, saveNewChannel

from display.forms.find_channel_form import findChannelForm
from display.forms.channel_form import UpdateChannelForm
from display.filters import OrderChannel

def channelsIndex(request):

    if request.method == 'POST':
        form = findChannelForm(request.POST)
        if form.is_valid():
            channelId = form.cleaned_data['channelId']
            # check if channel exists in db, otherwise fetch with youtube xml feed
            try:
                selectedChannel = Channel.objects.get(pk=channelId)
                # print("channel found in db")
                # display in another page
                return HttpResponseRedirect(reverse('channel-detail', args=[channelId]))
            except:
                # check if its a valid youtube channel, and asks if user want to save it and crawl it
                return HttpResponseRedirect(reverse('confirm-save-channel', args=[channelId]))

    else:
        form = findChannelForm()
    
    channels_list = Channel.objects.all().order_by('name')

    myFilter = OrderChannel(request.GET, queryset=channels_list)
    channels_list = myFilter.qs

    paginator = Paginator(channels_list, 15)

    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.page_number)
    data = {
        'form':form,
        'page_obj':page_obj,
        'paginator':paginator,
        'myFilter': myFilter,
    }

    return render(request, 'channel/index.html', context=data)

def channelDetail(request, channelId):
    try:
        selectedChannel = Channel.objects.get(pk=channelId)
    except:
        # the user isn't supposed to write the url manually
        messages.error(request, 'Channel associated with the ID not found on our database.')
        return HttpResponseRedirect(reverse('channel-index'))
        
    recentVideos = Video.objects.filter(channelId=selectedChannel).order_by('-publishedAt')
    paginator = Paginator(recentVideos, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'selectedChannel': selectedChannel,
        'page_obj':page_obj,
    }

    return render(request, 'channel/detail.html', context=data)

@login_required
def confirmSaveChannel(request, channelId):
    if request.method == 'POST':
        numOfVids = saveNewChannel(channelId)
        messages.success(request, 'Channel saved. %d archived video(s) found.' % (numOfVids))
        return HttpResponseRedirect(reverse('channel-update', args=[channelId]))

    else:
        channelTuple = isChannelExist(channelId)
        if channelTuple:
            data = {
                'fetchedChannel':channelTuple,
            }
            return render(request, 'channel/confirm_save_channel.html', context=data)
        else:
            messages.error(request, 'Channel associated with the ID not found on our database nor on YouTube.')
            return HttpResponseRedirect(reverse('channel-index'))

@login_required
def UpdateChannel(request, channelId):

    channel = Channel.objects.get(pk=channelId)
    form = UpdateChannelForm(instance=channel)

    if request.method == 'POST':
        form = UpdateChannelForm(request.POST, instance=channel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Channel updated.')
            return HttpResponseRedirect(reverse('channel-detail', args=[channelId]))
    context = {
        'selectedChannel':channel,
        'form':form,
    }
    return render(request, 'channel/update_form.html', context)

@login_required
def DeleteChannel(request, channelId):

    channel = Channel.objects.get(pk=channelId)
    channel.delete()
    messages.success(request, 'Channel %s deleted.' % channel)
    return HttpResponseRedirect(reverse('channel-index'))