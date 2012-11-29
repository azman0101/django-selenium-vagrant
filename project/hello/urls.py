from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'hello.views.basic_hello', name='basic_hello'),
)
