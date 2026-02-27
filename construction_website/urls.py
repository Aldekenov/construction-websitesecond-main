
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),  # для set_language
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls, name='login'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('images/', include('gallery_app.urls')),
    path("vacancies/", include("vacancies.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
