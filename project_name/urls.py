"""Project URL Configuration."""
from typing import List

from django.contrib import admin
from django.urls import URLPattern, path

urlpatterns: List[URLPattern] = [
    path("admin/", admin.site.urls),
]
