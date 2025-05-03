# user_urls.py
from django.urls import path
from app.views.profile_page import holdings, investing_plan

urlpatterns = [
    path('holdings/', holdings, name='holdings'),
    path('investing-plan/', investing_plan, name='investing_plan'),
]
