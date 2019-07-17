from django.urls import path
from django.conf import settings
from django.conf.urls import static

from ministry.contrib import views

urlpatterns = [
    path('crawl/', views.crawl, name='crawl'),
]


if settings.DEBUG:
    urlpatterns += static.static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
