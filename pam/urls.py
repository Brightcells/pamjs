from django.conf.urls import patterns, include, url

urlpatterns = patterns('pam.views',
    url(r'^pic/', 'pic', name='pic'),
    url(r'^aud/', 'aud', name='aud'),
    url(r'^mov/', 'mov', name='mov'),
)