# assets_urls.py
from django.urls import path
from app.views.auth_views import check_auth

urlpatterns = [
    path('auth/',check_auth),
]
