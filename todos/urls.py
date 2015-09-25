from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
   'todos.views',
    url(r'^$', 'index', name='index'),
    url(r'^api/v1/todo/$', 'post_collection'),

)