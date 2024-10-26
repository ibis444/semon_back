from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+i18n_patterns(
    path('', views.home, name='home'),  
    path('core/', include('core.urls')),  
    path('products/', include('products.urls')),  
    path('i18n/', include('django.conf.urls.i18n')), 
)

    
