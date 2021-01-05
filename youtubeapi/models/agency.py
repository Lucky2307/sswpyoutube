from django.db import models

class Agency(models.Model):

    """ 
    Agency that a talent may belong to,
    e.g.: hololive, nijisanji, voms, etc,
    if a channel doesn't belong in an agency, (null)
    they're an indie
    """
    name = models.CharField(max_length=100, null=False)
    icon = models.ImageField(null=True, blank=False, upload_to='agencies/')

    class Meta:
        app_label = 'youtubeapi'
        
    def __str__(self):
        return f'{self.name}'