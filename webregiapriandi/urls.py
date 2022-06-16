from django.contrib import admin
from django.urls import path, include
from webregi.views import AdsView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from webregi.sitemaps import PostSitemap
from webregi.views import page_not_found_view
from django.views.static import serve

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webregi.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('ads.txt', AdsView.as_view()),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

handler404 = "webregi.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)