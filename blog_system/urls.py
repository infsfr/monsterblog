from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'posts.views.index', name='index'),
    url(r'^post/(?P<slug>[-\w]+)/$', 'posts.views.post', name='post'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'categories.views.category',
        name='category'),
    url(r'^tag/(?P<slug>[-\w]+)/$', 'tags.views.tag', name='tag'),
    url(r'^page/(?P<page_number>[-\d]+)/$', 'posts.views.index', name='page'),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
