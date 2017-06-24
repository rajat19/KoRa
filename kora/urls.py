from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='account/index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^books/', include('books.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
