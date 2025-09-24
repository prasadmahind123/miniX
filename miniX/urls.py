from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.shortcuts import redirect
from django.contrib.auth.urls import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('/tweet/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
