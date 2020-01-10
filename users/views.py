from django.http import HttpResponse
from django.template import RequestContext
#from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
from django.http import Http404
from django.template import loader

def index(request):
    users = User.objects.all()

    template = loader.get_template('users/index.html')
    context = { 'users': users, }
    return HttpResponse(template.render(context, request))
    #return render_to_response('registration/index.html',{'users': users}, context_instance=RequestContext(request))

def detail(request, user_id):
    user = User.objects.get(pk=user_id)
    
    template = loader.get_template('users/detail.html')
    context = { 'users': users, }
    return HttpResponse(template.render(context, request))
    #return render_to_response('registration/detail.html',{'user': user}, context_instance=RequestContext(request))

#def register(request):

#def profile(request):
