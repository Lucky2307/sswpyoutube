from django import forms
from youtubeapi.models.agency import Agency

class CreateAgencyForm(forms.ModelForm):

    class Meta:
        model = Agency
        fields = '__all__'

    name = forms.CharField(label='Agency Name', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))