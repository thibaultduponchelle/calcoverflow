from django.db import models
from django.contrib.auth.models import User

class Medal(models.Model):
    name = models.CharField(max_length=40) # gold, silver or bronze (or something else)
    description = models.CharField(max_length=400) 
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
       return self.name

class Badge(models.Model):
    name = models.CharField(max_length=50)
    descritption = models.CharField(max_length=1600)
    medal = models.ForeignKey(Medal)
    bonus = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name

 
class UserBadge(models.Model):
    user = models.ForeignKey(User)
    badge = models.ForeignKey(Badge)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
       return ''
