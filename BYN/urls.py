# BYN/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your 'main' app's URLs. Assuming main/urls.py exists.
    # The empty string path means it will handle requests to the root URL (e.g., http://127.0.0.1:8000/)
    path('', include('main.urls')),
]

# This part is essential for serving static files in development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # If you also have media files uploaded by users, you'd add this:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)