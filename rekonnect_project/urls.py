from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', include('core.urls')),
    path('robots.txt', TemplateView.as_view(template_name='core/robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='core/sitemap.xml', content_type='application/xml')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
