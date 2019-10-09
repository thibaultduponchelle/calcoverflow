from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    reputation = models.IntegerField()
    remaining_votes = models.PositiveIntegerField()
    aboutme = models.CharField(max_length=2000)
    homepage = models.URLField(max_length=200)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
      UserProfile.objects.create(user=instance, reputation=0, remaining_votes=0, aboutme='', homepage='www.calcoverflow.com')

post_save.connect(create_user_profile, sender=User)



