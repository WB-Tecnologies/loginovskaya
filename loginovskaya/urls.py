from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('viewing-inside/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('1', TemplateView.as_view(template_name='steps/1.html')),
    path('2', TemplateView.as_view(template_name='steps/2.html')),
    path('3', TemplateView.as_view(template_name='steps/3.html')),
    path('4', TemplateView.as_view(template_name='steps/4.html')),
    path('5', TemplateView.as_view(template_name='steps/5.html')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
