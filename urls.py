"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.utils.translation import ugettext_lazy

from django.contrib import admin


admin.site.site_title = ugettext_lazy('Vocabulary')
admin.site.site_header = ugettext_lazy('Vocabulary')
admin.site.index_title = ugettext_lazy('Vocabulary admininstration')


urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns.append(url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                           'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT,
                            'show_indexes': True}))
