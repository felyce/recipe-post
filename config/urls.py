from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from lib.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('recipe/', include('recipe.urls')),
    path('comment/', include('comment.urls')),
    path('', IndexTemplateView.as_view(), name="index"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
