# assets_urls.py
from django.urls import path
from app.views.asset_page import asset_detail, asset_list, asset_mini_detail

urlpatterns = [
    path('list/', asset_list, name='asset-detail'),
    path('mini/<str:id>/', asset_mini_detail, name='asset-detail'),
    path('<str:id>/', asset_detail, name='asset-detail'),

]
