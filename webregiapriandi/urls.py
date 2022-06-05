from django.contrib import admin
from django.urls import path, include
from webregi.views import AdsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webregi.urls')),
    path('ads.txt', AdsView.as_view()),
]