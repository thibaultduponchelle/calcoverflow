from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^users/$', views.index),
    #url('^users/login/', 'django.contrib.auth.views.login', {'authentication_form': LoginForm, 'template_name': 'registration/login.html'}),
    #url('^users/logout/', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'}),
    url(r'^users/(?P<user_id>\d+)/$', views.detail),
]
