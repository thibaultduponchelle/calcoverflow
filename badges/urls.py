from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^badges/$', views.index),
    url(r'^badges/(?P<badge_id>\d+)/$', views.detail),
]
