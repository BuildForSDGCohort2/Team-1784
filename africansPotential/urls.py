from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('user/', include('users.urls')),
    path('profile/', include('profiles.urls')),
    path('discover/', include('discover.urls')),
    path('dashboard/', include('usersDashboard.urls')),
    path('froala_editor/',include('froala_editor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
