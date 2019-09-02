from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls import *
import profiles.urls
import accounts.urls
import KYPSamhita.urls
from . import views
admin.autodiscover()
# Personalized admin site settings like title and header
admin.site.site_title = "Appkyp Site Admin"
admin.site.site_header = "Appkyp Administration"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path("", include(accounts.urls)),
    path("governance/",include(KYPSamhita.urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^select2/', include('django_select2.urls')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]