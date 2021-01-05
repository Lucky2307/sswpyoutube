import django_filters
from django import forms

from youtubeapi.models.channel import Channel
from youtubeapi.models.language import Language
from youtubeapi.models.agency import Agency

class OrderChannel(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    language = django_filters.ModelMultipleChoiceFilter(
        queryset=Language.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False,
    )
    agency = django_filters.ModelChoiceFilter(
        queryset=Agency.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )
    class Meta:
        model = Channel
        exclude = ['channelId', 'icon', 'uploadPlaylist']