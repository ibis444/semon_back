from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
app_name='core'
urlpatterns = [
    
    path('',views.home , name="home"),
    path('contact/',views.contact , name="contact"),
    path('about/',views.about , name="about"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)