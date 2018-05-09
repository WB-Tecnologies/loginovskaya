from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('viewing-inside/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('inquire/', include('inquirers.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
