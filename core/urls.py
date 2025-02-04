from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from common.utils import redirect_to_admin

urlpatterns = [
    path("", redirect_to_admin),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
