from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^questions/$', views.index),
    url(r'^unanswered/$', views.unanswered),
    url(r'^questions/(?P<question_id>\d+)/$', views.detail),
    url(r'^questions/(?P<question_id>\d+)/answer/$', views.post_answer),
    url(r'^questions/ask$', views.ask_question),
    url(r'^questions/ask/post/$', views.post_question),
]
