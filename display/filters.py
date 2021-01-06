import django_filters
from django import forms

from youtubeapi.models.channel import Channel
from youtubeapi.models.language import Language
from youtubeapi.models.agency import Agency
from youtubeapi.models.video import Video

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

class OrderVideo(django_filters.FilterSet):

    start_date = django_filters.DateFilter(field_name="publishedAt", lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name="publishedAt", lookup_expr="lte")