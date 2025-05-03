# assets_urls.py
from django.urls import path
from app.views.auth_views import google_login, google_callback

urlpatterns = [
    path('google/login/',   google_login,    name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
]
