from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=400)
    content = models.CharField(max_length=1600)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    #is_resolved = models.BooleanField()
    votes = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    content = models.CharField(max_length=1600)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    #is_resolved = models.BooleanField()
    votes = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    question = models.ForeignKey('questions.Question', on_delete=models.PROTECT)

    def __unicode__(self):
        return self.content

