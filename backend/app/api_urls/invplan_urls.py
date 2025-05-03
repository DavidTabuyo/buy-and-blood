# assets_urls.py
from django.urls import path
from app.views.homepage import asset_list

urlpatterns = [
    path('best/', asset_list , name='asset-detail'),
]
