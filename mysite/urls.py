from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^todos/', include('todos.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
