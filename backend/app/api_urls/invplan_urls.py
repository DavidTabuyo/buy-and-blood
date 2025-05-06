# assets_urls.py
from django.urls import path
from app.views.homepage import best_plan

urlpatterns = [
    path('best/', best_plan , name='asset-detail'),
]
