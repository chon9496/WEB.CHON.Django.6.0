from django.contrib import admin
from django.urls import path,include

from django.conf import settings 
from django.conf.urls.static import static
from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    
    path('contacto/', include('contacto.urls',namespace='contacto')),
    path('curriculum/', include('curriculum.urls',namespace='curriculum')),
    
    
    
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)