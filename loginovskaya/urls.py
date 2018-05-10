from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path


urlpatterns = [
    path('viewing-inside/', admin.site.urls),
    path('', include('inquirers.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
