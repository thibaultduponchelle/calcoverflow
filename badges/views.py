from django.http import HttpResponse
from django.template import RequestContext
#from django.shortcuts import render_to_response
from badges.models import Badge
from badges.models import UserBadge
from questions.models import User
from django.template.context_processors import csrf
from django.http import Http404
from django.template import loader

def index(request):
    badges = Badge.objects.all().order_by('-pub_date')[:10]

    template = loader.get_template('badges/index.html')
    context = { 'badges': badges, }
    return HttpResponse(template.render(context, request))


def detail(request, badge_id):
    try:
      badge = Badge.objects.get(pk=badge_id)
    except:
      raise Http404
    ids = UserBadge.objects.filter(badge_id=badge.id).values('user_id')
    users = User.objects.filter(id__in = ids).order_by('-pub_date')[:10]
    template = loader.get_template('badges/detail.html')
    context = { 'badge': badge, 'users': users, }
    return HttpResponse(template.render(context, request))
