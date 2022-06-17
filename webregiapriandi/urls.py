from django.contrib import admin
from django.urls import path, include
from webregi.views import AdsView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from webregi.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('', include('webregi.urls')),
    path('ads.txt', AdsView.as_view()),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)