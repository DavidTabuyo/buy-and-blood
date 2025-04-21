
from django.contrib import admin
from django.urls import include, path
#views import
from app.views.homepage import prueba_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prueba/', prueba_view, name='prueba_api'),
    path('api/asset/', include('app.urls.assets_urls')),    
    path('api/invplan/', include('app.urls.invplan_urls')),    
]
