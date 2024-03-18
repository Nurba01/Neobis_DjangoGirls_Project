from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):

    #link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) 
    title = models.CharField(max_length = 200)
    text = models.TextField()
    #date and time
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    #the method of publishing for recording
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
    
