# assets_urls.py
from django.urls import path
from app.views.asset_page import asset_detail

urlpatterns = [
    path('<str:ticker>/', asset_detail, name='asset-detail'),
]
