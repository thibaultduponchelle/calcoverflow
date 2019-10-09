from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users.forms import LoginForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url('', include('questions.urls')),
    url('', include('badges.urls')),
    url('', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()



