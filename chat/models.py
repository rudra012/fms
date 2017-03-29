from __future__ import unicode_literals

from django.db import models

# Create your models here.
from users.models import User


class ChatMessage(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,null=True,blank=True)
    '''
    #commenting this too, as there are no user created channels, now there is only one public channel.
    channel = models.ForeignKey(Channel)
    '''
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message

'''
    This model will keeps track of chat clearing functionality by user. When ever we fetch users chat history,
    we ll check the last cleared timestamp and fetch the message records accordingly.
'''
class ChatClear(models.Model):
    last_cleared = models.DateTimeField(auto_now=True)
    cleared_by = models.ForeignKey(User)