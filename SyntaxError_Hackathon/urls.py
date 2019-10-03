
from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from AllInOne import views

urlpatterns = [
    url(r'^$', include('AllInOne.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^AllInOne/', include('AllInOne.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
