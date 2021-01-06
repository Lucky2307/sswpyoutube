from django.db import models

class Language(models.Model):

    """ 
    language(s) that a channel can speak 
    a channel may speak more than one language,
    so it's a many to many relationship.
    useful for sorting too i guess
    """
    name = models.CharField(max_length=100, null=False)
    icon = models.ImageField(null=True, blank=False, upload_to='flags_icon/')

    class Meta:
        app_label = 'youtubeapi'
        
    def __str__(self):
        return f'{self.name}'