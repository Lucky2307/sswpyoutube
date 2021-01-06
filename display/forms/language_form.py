from django import forms
from youtubeapi.models.language import Language

class CreateLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = '__all__'

    name = forms.CharField(label='Channel Name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))