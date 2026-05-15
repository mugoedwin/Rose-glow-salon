from django.contrib import admin
from pathlib import Path

from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from salon import views as salon_views

urlpatterns = [path("django-admin/", admin.site.urls)]

dist_dir = Path(settings.BASE_DIR) / "frontend" / "dist"

urlpatterns += [
    re_path(r"^assets/(?P<path>.*)$", serve, {"document_root": str(dist_dir / "assets")}),
    re_path(r"^images/(?P<path>.*)$", serve, {"document_root": str(dist_dir / "images")}),
]

# Catch-all: let the React router handle client-side routes.
urlpatterns += [re_path(r"^.*$", salon_views.react_app, name="react_app")]
