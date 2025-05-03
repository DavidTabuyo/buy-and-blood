# user_urls.py
from django.urls import path
from app.views.profile_page import holdings

urlpatterns = [
    path('holdings/', holdings, name='holdings'),
]
