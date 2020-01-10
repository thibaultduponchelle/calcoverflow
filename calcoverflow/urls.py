from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users.forms import LoginForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('', include('questions.urls')),
    url('', include('badges.urls')),
    url('', include('users.urls')),
    url(r'^users/login/$', auth_views.LoginView.as_view()),
    #url(r'^users/logout/$', auth_views.logout),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
]

urlpatterns += staticfiles_urlpatterns()



