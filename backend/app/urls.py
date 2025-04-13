
from django.contrib import admin
from django.urls import path
#views import
from app.views.homepage import prueba_view
from app.views.asset_page import asset_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prueba/', prueba_view, name='prueba_api'),
    path('api/asset/<str:ticker>/', asset_detail, name='asset-detail'),
]
