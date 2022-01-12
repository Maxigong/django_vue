from django.contrib import admin
from django.urls import path,re_path

from .views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
