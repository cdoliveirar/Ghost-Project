from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#class InformationType(models.Model):
class Topic(models.Model):    
    topic_name = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.topic_name)

    def get_absolute_url(self):
        return reverse('jobinformation:NoteList')
    
    class Meta:
        db_table = 'topic'


#class TextInformation(models.Model):
class Note(models.Model):
    topic = models.ForeignKey(Topic)
    text = models.CharField(max_length=1000)
    pup_date = models.DateTimeField('date published')
    
    def __str__(self):
        return '%s %s' % (self.text, self.pup_date)
    
    class Meta:
        db_table = 'note'