from django import forms
from youtubeapi.models.channel import Channel
from youtubeapi.models.language import Language
from youtubeapi.models.agency import Agency

class UpdateChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        exclude = ['icon', 'uploadPlaylist']

    channelId = forms.CharField(label='Channel ID', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'readonly': 'true'}))
    name = forms.CharField(label='Channel Name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control', 'readonly': 'true'}))
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )
    agency = forms.ModelChoiceField(
        queryset=Agency.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
